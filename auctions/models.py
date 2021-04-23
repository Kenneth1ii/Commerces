from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class AuctionBids(models.Model):
    CurrentBid = models.IntegerField()

    def __str__(self):
        return f"current bid price: {self.CurrentBid}"


class AuctionComment(models.Model):
    comment = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.comment}"


class AuctionListing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.TextField()
    bid = models.ForeignKey(AuctionBids, on_delete=models.CASCADE, related_name="auctionbidding", null=True)
    comments = models.ForeignKey(AuctionComment, on_delete=models.CASCADE, related_name="auctioncomment", null=True) 
    # Make nullable == null=true b/c we already created objects data before hand before we created bid/comment foreign keys ,
    # therefore we ran into constraint issues of default and nonnulliable.

    def __str__(self):
        return self.title

Categorylist = ['Books','Electronics','Trading Cards','Video Games','Other']

class AuctionCategory(models.Model):
    category = models.CharField(max_length=255)
    auctionlist = models.ManyToManyField(AuctionListing,related_name="category")

    def __str__(self):
        return f"{self.category}"