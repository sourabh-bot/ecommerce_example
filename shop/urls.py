from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='shop_home'),
    path('about/', about, name='AboutUs'),
    path('contact/', contact, name='ContactUs'),
    path('tracker/', tracker, name='TrackingStatus'),
    path('search/', search, name='Search'),
    path('productview/', productView, name='ProductView'),
    path('checkout/', checkout, name='Checkout'),
]