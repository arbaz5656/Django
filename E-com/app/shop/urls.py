from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home1,name="HomePage"),
    path('p&s/',views.proser,name="Product and Service"),
    path('media/',views.media,name="Media"),
    path('about/',views.about,name="About Us"),
    path('contact/',views.contact,name="Contact"),
]
