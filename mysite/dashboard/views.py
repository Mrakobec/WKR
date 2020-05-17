from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

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

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    else:
        return render(request, 'dashboard/logout.html')
