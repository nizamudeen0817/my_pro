from django.db import models
from ekartapp.models import Productcard
# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=255,blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    
class CartItem(models.Model):
    product = models.ForeignKey(Productcard,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.title