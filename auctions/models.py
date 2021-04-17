from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class AuctionCategory(models.Model):
    pass

class AuctionListing(models.Model):
    test = (
        ('Books', 'Books'),
        ('Video Games','Video Games'),
        ('Trading Cards','Trading Cards'),
        ('Others','Others'),
    )

    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.TextField()
    Categories = models.CharField(max_length=64, choices=test, default = 'Video Games' )#should be foreignkey instead

class AuctionBids(models.Model):
    CurrentBid = models.IntegerField()

class AuctionComment(models.Model):
    comment = models.CharField(max_length=255)