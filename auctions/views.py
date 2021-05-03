from django.contrib.auth import authenticate, login, logout 
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime , timedelta
from .models import *

@login_required
def index(request):
    return render(request, "auctions/index.html",{
        'auctionlisting': AuctionListing.objects.all().exclude(closed=True)
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
    userid = request.user.id
    user = User.objects.get(id=userid)

    def updatetime():
        listing.save()
        listing.auctiontimeremaining = listing.auctionendtime - listing.auctionstarttime
    updatetime()

    days = listing.auctiontimeremaining.days
    seconds = listing.auctiontimeremaining.seconds
    hours = seconds//3600
    minutes = (seconds//60)%60
    seconds =  seconds - ((hours*3600)+(minutes*60))

    watching = listing.userwatch.all().filter(id = userid).exists()

    def test():
        if watching:
            return 'Watching'
        else:
            return 'Add To Watchlist'
    test()

    testrender = render(request, "auctions/auctionlist.html", {
    "listing": listing,
    'watchstatus': test(),
    'commentlist': AuctionComment.objects.filter(auctioncomments=listing),
    'days': days,
    'seconds':seconds,
    'hours': hours,
    'minutes':minutes,
    })

    if request.method == 'POST':
        if request.POST.get('addwatch', False):
            if watching:
                watching = False
                user.userwatchlist.remove(listing)
                days = listing.auctiontimeremaining.days
                seconds = listing.auctiontimeremaining.seconds
                hours = seconds//3600
                minutes = (seconds//60)%60
                seconds = seconds ((hours*3600)+(minutes*60))
                return testrender      
            else:
                user.userwatchlist.add(listing)
                watching = True
                return testrender      

        if request.POST.get('current',False):
            a = int(request.POST["current"])
            if a <= listing.bid.currentBid:
                days = listing.auctiontimeremaining.days
                seconds = listing.auctiontimeremaining.seconds
                hours = seconds//3600
                minutes = (seconds//60)%60
                seconds =  seconds - ((hours*3600)+(minutes*60))
                return testrender
            else:
                listing.bid.currentBid = a
                listing.bid.currentuserbid = user
                listing.bid.save() # save foreign key reference first.
                days = listing.auctiontimeremaining.days
                seconds = listing.auctiontimeremaining.seconds
                hours = seconds//3600
                minutes = (seconds//60)%60
                seconds =  seconds - ((hours*3600)+(minutes*60))
                return testrender

        if request.POST.get('endlisting',False):
            winner = listing.bid.currentuserbid
            listing.userbought = winner
            listing.usersold = listing.owner
            listing.closed = True
            listing.save()

        if request.POST.get('comment',False):
            newComment = AuctionComment(comment=request.POST['comment'], auctioncomments = listing, usercommentlist=request.user)
            newComment.save()
    comment = AuctionComment.objects.filter(auctioncomments=listing)

    return testrender



def create_list(request):
    if request.method == "POST":
        c = AuctionBids(currentBid = request.POST['bid'])
        c.save()        
        category = request.POST['category']
        b = AuctionListing(title=request.POST['title'], description = request.POST['description'],image = request.POST['image'],bid= c)
        if AuctionCategory.objects.filter(category=category):
            e = AuctionCategory.objects.get(category=category)
            e.save()
            b.category = e
        else:
            f = AuctionCategory(category=category)
            f.save()
            b.category = f
        userid = request.user.id
        user= User.objects.get(id=userid)
        b.owner = user
        b.save()

        auctiontime = request.POST.get('auctionend',False)
        if auctiontime:
            starttime = b.auctionstarttime
            print(starttime)
            if auctiontime == '48 hrs':
                endtime = starttime + timedelta(days=2)
            else:
                endtime = starttime + timedelta(days=1)
        b.auctionendtime = endtime
        print(endtime)
        b.save()

        return HttpResponseRedirect(reverse('auctionlist', args=(b.id,) ))

    return render(request, "auctions/createlisting.html",{
        'Categories': Categorylist,
        'AuctionEnd': AuctionEnd,
    })

def watchlist(request):
    userid = request.user.id
    user = User.objects.get(id=userid)
    userwatchlist = user.userwatchlist.all()

    return render(request,'auctions/watchlist.html',{
        'userwatchlist': userwatchlist
    })

def purchase(request, id):
    userid = request.user.id
    user = User.objects.get(id=userid)
    userpurchases  = user.auctionbought.all()

    return render(request, 'auctions/purchase.html',{
        'userpurchases': userpurchases
    })