from django.contrib import admin
from .models import * # User from model.py class

# Register your models here.
admin.site.register(User)
admin.site.register(AuctionListing)
admin.site.register(AuctionBids)
admin.site.register(AuctionComment)