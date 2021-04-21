from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class AuctionListing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.TextField()

Categorylist = ['Books','Electronics','Trading Cards','Video Games','Other']

class AuctionCategory(models.Model):
    category = models.CharField(max_length=255)
    auctionlist = models.ManyToManyField(AuctionListing,related_name="category")


class AuctionBids(models.Model):
    CurrentBid = models.IntegerField()

class AuctionComment(models.Model):
    comment = models.CharField(max_length=255)