from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name="home"),
    path('test1/', views.test1, name='test1'),
]