from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('messages/', views.myMessages, name="myMessages"),
    path('subscriptions/', views.mySubs, name='mySubs'),
    path('payouts/', views.myPayouts, name='myPayouts'),
    path('support/', views.support, name='support'),
    path('contacts/', views.contacts, name='contacts'),
]
