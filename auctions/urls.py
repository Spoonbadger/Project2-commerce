from django.urls import path

from . import views

app_name = "auctions"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("listing/<str:title>/", views.listing, name="listing"),
    path("categories/", views.categories, name="categories"),
    path("watchlist/", views.watchlist, name="watchlist"),
    path("add_to_watchlist/<str:title>/", views.add_to_watchlist, name="add_to_watchlist"),
    path("remove_from_watchlist/<str:title>/", views.remove_from_watchlist, name="remove_from_watchlist"),
    path("new_bid/<int:id>", views.new_bid, name="new_bid"),
    path("close_auction/<int:id>", views.close_auction, name="close_auction"),
    path("wins_bids", views.wins, name="wins"),
    path("comments/<int:id>", views.comments, name="comments"),
]
