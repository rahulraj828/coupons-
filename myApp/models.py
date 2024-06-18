from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    discount_amount = models.DecimalField(max_digits=5, decimal_places=2)
    expiration_date = models.DateField()
    status = models.CharField(max_length=10, choices=[('available', 'Available'), ('sold', 'Sold'), ('swapped', 'Swapped')])
    owner = models.ForeignKey(User, related_name='coupons', on_delete=models.CASCADE)

class Transaction(models.Model):
    buyer = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon, related_name='transactions', on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)

class Swap(models.Model):
    requester = models.ForeignKey(User, related_name='requested_swaps', on_delete=models.CASCADE)
    requested_coupon = models.ForeignKey(Coupon, related_name='requested_swaps', on_delete=models.CASCADE)
    offered_coupon = models.ForeignKey(Coupon, related_name='offered_swaps', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined')])
    swap_date = models.DateTimeField(auto_now_add=True)

