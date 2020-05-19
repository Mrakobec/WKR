from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Person

# def test1(request):
#     return render(request, 'test1/test.html')

# получение данных из бд
def index(request):
    people = Person.objects.all()
    return render(request, "test1/index.html", {"people": people})

# сохранение данных в бд
def create(request):
    if request.method == "POST":
        tom = Person()
        tom.name = request.POST.get("name")
        tom.age = request.POST.get("age")
        tom.save()
    return HttpResponseRedirect("/test1")

# изменение данных в бд
def edit(request, id):
    try:
        person = Person.objects.get(id=id)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/test1")
        else:
            return render(request, "test1/edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/test1")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
# Create your views here.
