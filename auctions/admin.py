from django.contrib import admin
from .models import * # User from model.py class

class FlightAdmin(admin.ModelAdmin):
    list_display = ('title','description','image','category')

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("auctionlist",)
# Register your models here.


admin.site.register(User)
admin.site.register(AuctionListing,FlightAdmin)
admin.site.register(AuctionBids)
admin.site.register(AuctionCategory,PassengerAdmin)
admin.site.register(AuctionComment)