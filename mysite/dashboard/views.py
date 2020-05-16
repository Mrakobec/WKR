from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'dashboard/home.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

@login_required
def myMessages(request):
    return render(request, 'dashboard/myMessages.html')

@login_required
def mySubs(request):
    return render(request, 'dashboard/mySubs.html')

@login_required
def myPayouts(request):
    return render(request, 'dashboard/myPayouts.html')

@login_required
def support(request):
    return render(request, 'dashboard/support.html')

@login_required
def contacts(request):
    return render(request, 'dashboard/contacts.html')
