from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("",views.index, name = "home" ),
    path('about',views.about, name= "about" ),
    path('service',views.service, name= "service" ),
    path('contact',views.contact, name= "contact" ),
    path('login',views.loginuser, name= "login" ),
    path('amount', views.amount, name= "amount"),
    path('register', views.register, name= 'register'),
    path('payment', views.payment, name="payment"),
    path('logout', views.logoutuser, name="logout")
]
