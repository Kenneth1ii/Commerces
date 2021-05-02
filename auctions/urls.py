from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('createlist',views.create_list,name="createlist"),
    path("auctionlist/<str:id>", views.auction_list, name="auctionlist" ),
    path("watchlist",views.watchlist, name='watchlist'),
    path('purchase/<str:id>', views.purchase, name='purchase'),
]
