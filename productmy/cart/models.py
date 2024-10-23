from django.db import models
from django.contrib.auth import get_user_model
from app.models import Product

User = get_user_model
сlass CartUser(models.Model):
    user = models.OneTooneField(User, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeigKey(CartUser,on_delete=models.CASCADE)
    product = models.ForeigKey(Product,on_delete=models.CASCADE)
    quantity = models.InterField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']