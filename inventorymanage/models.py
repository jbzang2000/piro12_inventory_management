from django.db import models
from inventory.utils import uuid_upload_to

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    image = models.ImageField(blank=True, upload_to=uuid_upload_to)
    shops = models.CharField(max_length=100)


class Shop(models.Model):
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    items = models.ManyToManyField(Item, blank=True)
