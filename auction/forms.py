from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Bid, Item, Payment, Person
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ["date_created"]
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'E-mail Address',
            'phone': 'Phone',
        }
        widgets = {
        'first_name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder':'Enter first name', 'required': True}),
        'last_name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder':'Enter last name', 'required': True}),
        'email': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder':'Enter e-mail address', 'required': False}),
        'phone': forms.NumberInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder':'Enter phone number', 'required': True}),
        }      
        

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ["date_added"]
        labels = {
            'name': 'Item Name',
            'price': 'Price',
            'item_description': 'Item Description',
            'category': 'Item Category',
        }
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder':'Enter item name', 'required': True}),
        'category': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder':'Enter item category', 'required': True}),
        'price': forms.NumberInput(attrs={'class': 'form-control', 'type': 'text', 'max_length':30, 'placeholder':'Enter price of item', 'decimal_places':2, 'required': True}),
        'item_description': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'max_length':100, 'placeholder':'Enter item description', 'required': True}),
        }      
        

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        exclude = ["date_placed"]
        labels = {
            'user': 'Name of Bidder',
            'item': 'Bidding Item',
            'offer': 'Offer',
        }
        widgets = {
        'user': forms.Select(attrs={'class': 'form-control', 'type': 'text', 'placeholder':'Enter user name', 'required': True}),
        'offer': forms.NumberInput(attrs={'class': 'form-control', 'type': 'text', 'max_digits':30, 'placeholder':'Enter bid', 'decimal_places':2, 'required': True}),
        'item': forms.Select(attrs={'class': 'form-control', 'type': 'text', 'max_length':100, 'placeholder':'Enter the item you are bidding', 'required': True}),
        }      
        

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payment_method', 'acc_number', 'payment_amount']
        labels = {
            'acc_number': 'Account Number',
                }
        widgets = {
            'payment_method': forms.Select(attrs={'class': 'form-control', 'type': 'text', 'placeholder':'Enter payment type', 'required': True}),
            'acc_number': forms.NumberInput(attrs={'max_digits': 20, 'class': 'form-control', 'type': 'text', 'max_digits':20, 'placeholder':'Enter account number', 'decimal_places':2, 'required': True}),
            'payment_amount': forms.NumberInput(attrs={'max_digits': 20, 'class': 'form-control', 'type': 'text', 'max_digits':20, 'placeholder':'Enter payment amount', 'decimal_places':2, 'readonly': True}),
        }
