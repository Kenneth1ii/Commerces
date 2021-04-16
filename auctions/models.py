from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class AuctionListing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()

class AuctionBids(models.Model):
    CurrentBid = models.IntegerField()

class AuctionComment(models.Model):
    comment = models.CharField(max_length=255)