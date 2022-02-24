from django import views
from django.urls import path
from . import views

app_name='reseller'

urlpatterns = [
    path('reseller-home',views.reseller_home,name='reseller_home')
]