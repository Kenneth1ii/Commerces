from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *


def index(request):
    return render(request, "auctions/index.html",{
        'auctionlisting': AuctionListing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def auction_list(request, id):
    listing = AuctionListing.objects.get(pk=id)
    try:
        if listing.watch.watching.userwatch.id:
            watchstatus = "Watching"
            watching = True
    except AttributeError:
        watchstatus = "Add to Watchlist"
        watching = False

    if request.method == "POST":

        if request.POST["addwatch"]:
            if watching:
                User.userwatchlist.remove(listing.watch)
                return render(request, "auctions/auctionlist.html", {
                    "listing": listing,
                    "watchstatus": watchstatus
                })              

                listing.watch.watching = True
                return render(request, "auctions/auctionlist.html", {
                    "listing": listing,
                    "watchstatus": watchstatus
                })                


        if request.POST["current"]:
            a = int(request.POST["current"])
            if a <= listing.bid.currentBid:
                return render(request, 'auctions/auctionlist.html',{
                    "listing": listing,
                    "message": 'Your Current bid does not meet the minimum'
                })
            else:
                listing.bid.currentBid = a
                listing.bid.save() # save foreign key reference first.
                return render(request, "auctions/auctionlist.html", {
                "listing": listing,
                })

    return render(request, "auctions/auctionlist.html", {
        "listing": listing,
        "watchstatus": watchstatus
    })

def create_list(request):
    if request.method == "POST":
        a = AuctionCategory(category = request.POST['category'])
        a.save()
        c = AuctionBids(currentBid = request.POST['bid'])
        c.save()
        d = AuctionWatch()
        d.save()
        b = AuctionListing(title=request.POST['title'], description = request.POST['description'],image = request.POST['image'],bid= c,watch=d)
        b.save()
        a.auctionlist.add(b)
        
        
        return HttpResponseRedirect(reverse('auctionlist', args=(b.id,) ))
    
    return render(request, "auctions/createlisting.html",{
        'Categories': Categorylist,
    })
