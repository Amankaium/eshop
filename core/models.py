from django.db import models


class Good(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    qty = models.IntegerField(default=0)


class Order(models.Model):
    description = models.TextField()
    phone_number = models.CharField(max_length=50)
    
