from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Listing, Category


def categories(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "auctions/categories.html", {
            "categories": categories,
        })
    else:
        selected_category_id = request.POST['selected_category']
        selected_category = Category.objects.get(pk=selected_category_id)
        category_listings = Listing.objects.filter(isActive=True, category=selected_category)
        return render(request, "auctions/index.html", {
            "listings": category_listings
        })


def create_listing(request):
    if request.method == "GET":
        allCategories = Category.objects.all()
        return render(request, "auctions/create_listing.html", {
            "categories": allCategories,
        })
    else:
        try:
            title = request.POST['listing_title']
            description = request.POST['listing_description']
            imageURL = request.POST['listing_image_url']
            price = request.POST['listing_start_price']
            category = request.POST['listing_category']
            categoryData = Category.objects.get(categoryName=category)
            currentUser = request.user
            # Create new listing
            newListing = Listing(
                title=title,
                description=description,
                imageURL=imageURL,
                price=float(price),
                category=categoryData,
                seller=currentUser
            )
            newListing.save()
            return HttpResponseRedirect(reverse("auctions:index"))
        except ValueError as e:
            print(f"Value Error: {e}") 


def index(request):
        active_listings = Listing.objects.filter(isActive=True)
        return render(request, "auctions/index.html", {
            "listings": active_listings,
        })


def listing(request, title):
    if request.method == "GET":
        if request.user.is_authenticated:
            requested_listing = Listing.objects.get(title=title)
            watchlisted = False
            user = request.user
            if requested_listing in user.watchlist.all():
                watchlisted = True
            return render(request, "auctions/listing.html", {
                "listing": requested_listing,
                "watchlisted": watchlisted,
            })
        else:
            requested_listing = Listing.objects.get(title=title)
            return render(request, "auctions/listing.html", {
                "listing": requested_listing,
            })
        


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("auctions:index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("auctions:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, ("auctions/register.html"), {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def watchlist(request):
    if request.user.is_authenticated:
        # Get all the listings in the watchlist, get user first
        user = request.user
        watchlistings = user.watchlist.all()
        return render(request, ("auctions/watchlist.html"), {
            "watchlistings": watchlistings
        })



def add_to_watchlist(request, title):
    if request.method == "POST":
        if request.user.is_authenticated:
            # I need to get the user, get the listing, add listing to watchlist
            user = request.user
            listing = Listing.objects.get(title=title)
            user.watchlist.add(listing)
            return HttpResponseRedirect(reverse("auctions:listing", args=(title, )))
        else:
            return redirect("auctions/listing.html")


def remove_from_watchlist(request, title):
    if request.method == "POST":
        if request.user.is_authenticated:
            user = request.user
            listing = Listing.objects.get(title=title)
            user.watchlist.remove(listing)
    return HttpResponseRedirect(reverse("auctions:listing", args=(title, )))