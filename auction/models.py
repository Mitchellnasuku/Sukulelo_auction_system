from datetime import timezone
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=13, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Item(models.Model):
    CATEGORY = (
        ('Home Equipment', 'Home Equipment'),
        ('Office Equipment', 'Office Equipment'),
        ('Cars', 'Cars'),
        ('Clothes', 'Clothes'),
    )
    name = models.CharField(max_length=20, null=False, blank=False)
    category = models.CharField(max_length=50, null=False, blank=False, choices=CATEGORY)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "%s " % (self.name)
    
    
class Bid(models.Model):
    Status = (
        ('Won Bid', 'Won Bid'),
        ('Current Bid', 'Current Bid'),
        ('Outbid', 'Outbid'),
        ('Lost Bid', 'Lost Bid'),
    )
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
    )
    user = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL, related_name='bids')
    item = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL, related_name='auction_item')
    offer = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.CharField(max_length=50, null=False, blank=False, choices=Status, default='Current Bid')
    payment_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    date_placed = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
     return f"Bid for {self.item} by {self.user}"
 
 
class Payment(models.Model):
    PAYMENT_CHOICES = (
        ('PAYPAL', 'PAYPAL'),
        ('VISA CARD', 'VISA CARD'),
        ('MASTERCARD', 'MASTERCARD'),
    )
    bid = models.OneToOneField(Bid, on_delete=models.CASCADE, related_name='payment')
    payment_method = models.CharField(max_length=50, choices=PAYMENT_CHOICES, null=True, blank=True)
    payment_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    acc_number = models.DecimalField(max_digits=20, decimal_places=0, null=True, blank=True)

    def __str__(self):
        return f"Payment for Bid: {self.bid.id}"