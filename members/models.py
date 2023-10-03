from django.db import models
from datetime import date

class Item(models.Model):
    UNIT_CHOICES = [
        ("KG", "kg"),
        ("TON", "t"),
        ("G", "g"),
        ("MG", "mg"),
        ("LB", "lb"),
        ("OZ", "oz"),
        ("L", "l"),
        ("KL", "kl"),
        ("ML", "ml"),
        ("PCS", "pcs")
    ]  
    date = models.DateField(default=date.today())
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    price_unit = models.CharField(max_length=4, choices=UNIT_CHOICES)
    yesterday_price = models.IntegerField(null=True)
    stock = models.IntegerField()
    stock_unit = models.CharField(max_length=4, choices=UNIT_CHOICES)
    description = models.CharField(max_length=255)

class News(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=300)
    long_description = models.CharField(max_length=16000)

# item = Item(name='Beras 1', price='100000', yesterday_price="10", stock = "10", description="HI")