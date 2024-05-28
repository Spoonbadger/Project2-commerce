from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Auction_listings():
    starting_price = ...
    current_bid = ...
    sale_price = ...



class bids():
    ...


class listing_comments():
    comment = ...
    comment_by_username = ...
    



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