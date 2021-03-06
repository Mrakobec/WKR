from django.urls import path, re_path
from . import views

urlpatterns = [
    #path('', views.home, name="home"),
    path('', views.dashboard, name='dashboard'),
    path('messages/', views.myMessages, name="myMessages"),
    # path('subscriptions/', views.mySubs, name='mySubs'),
    path('payouts/', views.myPayouts, name='myPayouts'),
    path('support/', views.support, name='support'),
    path('contacts/', views.contacts, name='contacts'),
    path('input/', views.input),
    path('messages/<int:fpk>/', views.MessagesFilter, name='MessagesFilter'),
    path('payouts/<int:fpk>/', views.OutPutFilter, name='OutPutFilter'),
    # path('users/', views.users),
    # path('users/create/', views.userscreate),
    # path('users/edit/<int:id>/', views.usersedit),
    # path('users/delete/<int:id>/', views.usersdelete),
    #path('r/<str:username>/', views.InPut_create_view, name='inpustcreate'),
    # path('input/create/', views.inputcreate),
    # path('inputcreate/', views.InPut_create_view, name='inputcreate'),
    # path('balancecreate/', views.addbalance),
    # path('balanceedit/', views.createbalance),
    # path('balance/', views.viewbalance),
    # path('outputcreate/', views.OutPutCreate)
    # path('landing/', views.landing, name="landing")

]
