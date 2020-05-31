from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import InPut, Userss, User
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .forms import InputForm
import time

def home(request):
    return render(request, 'dashboard/home.html')

@login_required
def dashboard(request):
    print(request.user)
    return render(request, 'dashboard/dashboard.html')

@login_required
def myMessages(request):
    pay = InPut.objects.filter(user=request.user)
    return render(request, 'dashboard/myMessages.html', {"pay":pay})

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

def payin(request):
    return render(request, 'dashboard/r.html')
def users(request):
    people = User.objects.all()
    return render(request, 'dashboard/users.html', {"people": people})

def userscreate(request):
    if request.method == "POST":
        tom = User()
        tom.username = request.POST.get("nickname")
        tom.save()
    return HttpResponseRedirect("/dashboard/users/")
# изменение данных в бд
def usersedit(request, id):
    try:
        person = User.objects.get(id=id)

        if request.method == "POST":
            person.username = request.POST.get("name")
            person.save()
            return HttpResponseRedirect("/dashboard/users/")
        else:
            return render(request, "dashboard/usersedit.html", {"person": person})
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def usersdelete(request, id):
    try:
        person = User.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/dashboard/users/")
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

def input(request):
    pay = InPut.objects.all()
    return render(request, 'dashboard/input.html', {"pay": pay})

def inputcreate(request):
    # try:
    #     tom = User.objects.get(id=id)

    if request.method == "POST":
        tom = InPut()
        tom.user = request.POST.get("user")
        tom.date = time.ctime
        tom.name = request.POST.get("name")
        tom.amount = request.POST.get("amount")
        tom.currency = 1

        amounted = float(tom.amount)
        comiss1 = round((amounted * 0.05), 2)
        comiss2 = round((amounted * 0.01), 2)
        amount_end = amounted - comiss1 - comiss2
        print(amounted)
        print(comiss1)
        print(comiss2)
        print(amount_end)
        tom.comiss1 = comiss1
        tom.comiss2 = comiss2
        tom.amount_end = amount_end

        # tom.comiss1 = tom.amount*0.05
        # tom.comiss2 = tom.amount*0.01
        # tom.amount_end = tom.amount - tom.comiss1 - tom.comiss2
        tom.text = request.POST.get("text")
        tom.status = 1
        tom.save()
    return HttpResponseRedirect("/dashboard/input/")

def InPut_create_view(request):
    my_form = InputForm(request.POST or None)
    if my_form.is_valid():
        if request.method == "POST":
            my_new_amount = request.POST.get('amount')
            if my_new_amount != None:
                # pay.date = time.ctime
                amounted = float(my_new_amount)
                comiss1 = round((amounted * 0.05), 2)
                comiss2 = round((amounted * 0.01), 2)
                amount_end = amounted - comiss1 - comiss2
                print(my_new_amount)
                print(comiss1)
                print(comiss2)
                print(amount_end)
            instance = my_form.save(commit=False)
            instance.comiss1 = comiss1
            instance.comiss2 = comiss2
            instance.amount_end = amount_end
            instance.save()
            my_form = InputForm()


            # save article to db
    context = {
        'form': my_form
    }
    return render(request, "dashboard/InPut_create.html", context)

# def InPut_create_view(request):
#     form = InputForm(request.POST or None)
#     if form.is_valid():
#
#         form = InputForm()
#         if request.method == "POST":
#             my_new_amount = request.POST.get('amount')
#             if my_new_amount != None:
#                 pay = InPut.objects
#                 # pay.date = time.ctime
#                 amounted = float(my_new_amount)
#                 comiss1 = round((amounted * 0.05), 2)
#                 comiss2 = round((amounted * 0.01), 2)
#                 pay.date = time.ctime
#                 amount_end = amounted - comiss1 - comiss2
#                 print(my_new_amount)
#                 print(comiss1)
#                 print(comiss2)
#                 print(amount_end)
#                 pay.comiss1 = comiss1
#                 pay.comiss2 = comiss2
#                 pay.amount_end = amount_end
#                 pay.save()
#                 form.save()
#
#             else:
#                 print('None')
#     context = {
#         'form': form
#     }
#     return render(request, "dashboard/InPut_create.html", context)

# def InPut_create_view(request):
#     print(request.GET)
#     print(request.POST)
#     if request.method == "POST":
#         my_new_amount = request.POST.get('amount')
#         if my_new_amount != None:
#             comiss = round((float(my_new_amount) * 0.05), 2)
#             print(my_new_amount)
#             print(comiss)
#         else:
#             print('None')
#     context = {}
#     return render(request, "dashboard/InPut_create.html", context)
# def InPut_create_view(request):
#     form =
#     if form.is_valid():
#         my_new_amount = request.POST.get('amount')
#         #         if my_new_amount != None:
#         #             comiss = round((float(my_new_amount) * 0.05), 2)
#         #             print(my_new_amount)
#         #             print(comiss)
#         #         else:
#         #             print('None')
#     context = {
#     }
#     return render(request, "dashboard/InPut_create.html", context)

