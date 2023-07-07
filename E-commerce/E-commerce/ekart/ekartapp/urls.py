from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('products',views.products,name='products'),
    path('booking',views.Booking,name='booking'),
    
]