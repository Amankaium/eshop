from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    test = models.BooleanField(default=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Category(models.Model):
    name = models.CharField(max_length=255)
    updated_at = models.DateTimeField(null=True, auto_now_add=True)


class Good(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    qty = models.IntegerField(default=0)
    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL,
        null=True, blank=True,
    )


class Order(models.Model):
    user = models.ForeignKey(
        to=User,
        related_name="order",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    goods = models.ManyToManyField(
        to=Good,
        related_name="order",
        blank=True
    )

    description = models.TextField()
    phone_number = models.CharField(max_length=50)
    
