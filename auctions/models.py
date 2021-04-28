from django.contrib.auth.models import AbstractUser
from django.db import models


class AuctionBids(models.Model):
    currentBid = models.IntegerField()
    
    def __str__(self):
        return f"current bid price: {self.currentBid}"


class AuctionComment(models.Model):
    comment = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.comment}"

Categorylist = ['Books','Electronics','Trading Cards','Video Games','Other']
class AuctionCategory(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.category}"

class AuctionListing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.TextField()
    bid = models.ForeignKey(AuctionBids, on_delete=models.CASCADE, related_name="auctionbidding", null=True)
    comments = models.ForeignKey(AuctionComment, on_delete=models.CASCADE, related_name="auctioncomment", null=True) 
    # Make nullable == null=true b/c we already created objects data before hand before we created bid/comment foreign keys ,
    # therefore we ran into constraint issues of default and nonnulliable
    category = models.ForeignKey(AuctionCategory,on_delete=models.CASCADE, related_name="auctioncategory", null=True)
    def __str__(self):
        return self.title

class User(AbstractUser,models.Model):
    userwatchlist = models.ManyToManyField(AuctionListing, related_name="userwatch", blank=True)
    usercommentlist = models.ManyToManyField(AuctionComment,related_name="usercomment", blank=True )






