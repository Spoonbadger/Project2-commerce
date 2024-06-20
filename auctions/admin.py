from django.contrib import admin

# Register your models here.
from .models import Bids, Comments, Listing, Category, User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email',]
    filter_horizontal = ("watchlist",)

admin.site.register(User, UserAdmin)
admin.site.register(Listing)
admin.site.register(Category)
admin.site.register(Bids)
admin.site.register(Comments)