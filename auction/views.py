from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from django.urls import reverse
from .filters import BidFilter
from auction.models import Bid, Payment
from .forms import BidForm, Item, ItemForm, Person, PaymentForm
from django.http import HttpResponse
from django.contrib import messages
from auction.forms import UserForm
from django.db.models import Max




from django.shortcuts import redirect
def custom_login_redirect(request):return redirect('http://127.0.0.1:8000/dashboard/')




def dashboard(request):
    user = Person.objects.all()
    item = Item.objects.all()
    bid = Bid.objects.all()
    
    total_users = user.count()
    total_items = item.count()
    total_bids = bid.count()
    
    context = {'user': user, 'item': item, 'bid': bid, 'total_users': total_users, 
               'total_items': total_items, 'total_bids': total_bids}
    return render(request, 'auction/dashboard.html', context)


def view_user(request, id):
    user = Person.objects.get(id=id) 
    bid = user.bids.all()
    bid_count = bid.count()
    paid_bids = user.bids.filter(payment_status='Paid').count() 
    
    myFilter = BidFilter(request.GET, queryset=bid)
    bid = myFilter.qs
    
    context = {'user': user, 'bid': bid, 'bid_count': bid_count, 'myFilter': myFilter, 'paid_bids': paid_bids}
    return render(request, 'auction/user.html', context)
    
def items(request):
    items = Item.objects.all()
    
    context = {'items': items}
    return render(request, 'auction/item.html', context)

def create_user(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'User has been created successfully')
        return redirect('/dashboard')
    context = {'form':form}
    return render(request, 'auction/create_form.html', context)

def update_user(request, id):
    user = Person.objects.get(id=id)
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User has been updated successfully')
            return redirect('/dashboard')
    context = {'form':form}
    return render(request, 'auction/create_form.html', context)


def delete_user(request, id):
    user = Person.objects.get(id=id)
    user.delete()
    return redirect("auction/dashboard")


def create_item(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Item has been created successfully')
        return redirect('/dashboard')
    context = {'form':form}
    return render(request, 'auction/create_form.html', context)

def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(instance=item)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item has been updated successfully')
            return redirect('/dashboard')
    context = {'form':form}
    return render(request, 'auction/create_form.html', context)


def delete_item(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect("/dashboard")


def create_bid(request):
    form = BidForm()
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            new_bid = form.save(commit=False)
            # Check if the bid amount is greater than existing bids for the same item
            existing_bids = Bid.objects.filter(item=new_bid.item)
            max_bid = existing_bids.aggregate(Max('offer'))['offer__max']
            
            if max_bid is not None and new_bid.offer > max_bid:
                # Set the status of all existing bids for the same item to 'Outbid'
                existing_bids.update(status='Outbid')
                new_bid.status = 'Won Bid'
            else:
                new_bid.status = 'Current Bid'
            
            new_bid.save()
            messages.success(request, 'Bid has been created successfully')
            return redirect('/dashboard')
    context = {'form': form}
    return render(request, 'auction/create_form.html', context)

def update_bid(request, id):
    bid = Bid.objects.get(id=id)
    form = BidForm(instance=bid)
    if request.method == 'POST':
        form = BidForm(request.POST, instance=bid)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bid has been updated successfully')
            return redirect('/dashboard')
    context = {'form':form}
    return render(request, 'auction/create_form.html', context)


def delete_bid(request, id):
    bid = Bid.objects.get(id=id)
    bid.delete()
    return redirect('/dashboard')


def make_payment(request, id):
    bid = Bid.objects.get(id=id)
    user_id = bid.user.id  # Get the user ID associated with the bid
    
    if bid.status == 'Won Bid':
        if bid.payment_status == 'Paid':
            messages.warning(request, "Payment has already been made for this bid!")
            return redirect(reverse('view_user', args=[user_id]))
        
        if request.method == 'POST':
            form = PaymentForm(request.POST)
            if form.is_valid():
                payment = form.save(commit=False)
                payment.bid = bid
                payment.payment_amount = bid.offer
                payment.save()
                bid.payment_status = 'Paid'
                bid.save()
                messages.success(request, 'Payment has been made successfully')
                return redirect(reverse('view_user', args=[user_id]))
        else:
            item_name = bid.item.name
            price = bid.item.price
            offer = bid.offer
            form = PaymentForm(initial={'payment_amount': offer})
            context = {
                'item_name': item_name,
                'price': price,
                'offer': offer,
                'form': form
            }
            return render(request, 'auction/create_form.html', context)
    else:
        messages.warning(request, "You can only make payment for a bid that you have won!")
        return redirect(reverse('view_user', args=[user_id]))