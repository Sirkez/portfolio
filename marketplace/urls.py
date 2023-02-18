from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (AuctionCreateView, MarketplaceListView, AuctionDetailView, CategoryListView,
                    WatchlistView, MyAuctionsListView, MyAuctionUpdateView, MyAuctionDeleteView)

urlpatterns = [
     path('',
         MarketplaceListView.as_view(),
         name='index' ),
     path('create/',
         AuctionCreateView.as_view(),
         name='create'),
     path('auction/<str:pk>/<slug:slug>', AuctionDetailView.as_view(), name='auction'),
     path('category/<str:category>/', CategoryListView.as_view(), name='category'),
     path('watchlist/', WatchlistView.as_view(), name='watchlist'),
     path('my_auctions/', MyAuctionsListView.as_view(), name='my_auctions'),
     path('update/<int:pk>/', MyAuctionUpdateView.as_view(), name='update'),
     path('delete/<int:pk>',MyAuctionDeleteView.as_view(),name='delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
