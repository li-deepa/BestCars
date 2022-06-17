from django import views
from django.urls import path
from .views import*

urlpatterns = [
   
    path('', views.home, name='home'),
     path('contact', views.contact, name='contact'),
      path('about', views.about, name='about'),

]
