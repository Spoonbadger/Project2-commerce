from django.contrib.auth.models import AbstractUser
from django.db import models


class Bid(models.Model):
    new_bid = models.DecimalField(max_digits=10, blank=True, decimal_places=2)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} new bid: ${self.new_bid}"

class Category(models.Model):
    category_name = models.CharField(max_length=64)

    def __str__(self):
        return self.category_name
    

class Comments(models.Model):
    comment = ...
    user = ...
    item_listing = models.ForeignKey('Listing', on_delete=models.SET_NULL, null=True)


class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    imageURL = models.URLField(max_length=200, blank=True)
    current_bid = models.ForeignKey('Bid', on_delete=models.CASCADE, related_name="listing", default=0)
    is_active = models.BooleanField(default=True)
    seller = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, related_name="seller")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="category")

    def __str__(self):
        return self.title


class User(AbstractUser):
    watchlist = models.ManyToManyField('Listing', blank=True, related_name="user_watching")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



"""
You will also need to add additional models to this file to represent details about auction listings, bids, comments, and auction categories. 
Remember that each time you change anything in auctions/models.py, 
you’ll need to first run python manage.py makemigrations 
and then python manage.py migrate to migrate those changes to your database.
"""
"""
Models: Your application should have at least three models in addition to the User model: 
one for auction listings, one for bids, and one for comments made on auction listings. 
It’s up to you to decide what fields each model should have, and what the types of those fields should be.
"""
