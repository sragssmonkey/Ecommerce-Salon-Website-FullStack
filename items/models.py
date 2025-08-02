from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='items/')
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    description=models.TextField()
    sold = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    thing=models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.thing.price*self.quantity