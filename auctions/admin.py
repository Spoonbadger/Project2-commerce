from django.contrib import admin

# Register your models here.
from .models import Listing, Category, User


admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Category)