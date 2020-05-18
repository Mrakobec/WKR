from django.shortcuts import render

def test1(request):
    return render(request, 'test1/test.html')
# Create your views here.
