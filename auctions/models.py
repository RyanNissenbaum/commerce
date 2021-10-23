from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    starting_bid = models.DecimalField(max_digits=9,decimal_places=2)
    ##image_url = forms.ImageField()

    def __str__(self):
        return f"({self.id}) - Category: {self.category}{chr(10)}Title: {self.title}{chr(10)}Description: {self.description}{chr(10)}Starting Bid: {self.starting_bid}"