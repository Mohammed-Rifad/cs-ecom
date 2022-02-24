from django import views
from django.urls import path
from . import views

app_name='customer'

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('verifyotp', views.verify_otp, name='verify_otp'),
    path('home',views.customer_home,name='cust_home'),
    path('logout',views.cust_logout,name='logout')
]