from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Bids(models.Model):
    current_bid = ...
    all_bids = ...
    starting_bid = ...


class Category(models.Model):
    categoryName = models.CharField(max_length=64)

    def __str__(self):
        return self.categoryName
    

class Comments(models.Model):
    comment = ...
    user = ...
    item_listing = ...


class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    imageURL = models.URLField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    isActive = models.BooleanField(default=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="seller")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, related_name="category")
    watchlist = models.ManyToManyField(User, blank=True, related_name="watchlist_users")

    def __str__(self):
        return self.title




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
