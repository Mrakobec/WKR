from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'dashboard/home.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def myMessages(request):
    return render(request, 'dashboard/myMessages.html')

def mySubs(request):
    return render(request, 'dashboard/mySubs.html')

def myPayouts(request):
    return render(request, 'dashboard/myPayouts.html')

def support(request):
    return render(request, 'dashboard/support.html')

def contacts(request):
    return render(request, 'dashboard/contacts.html')
