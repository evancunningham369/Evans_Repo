from django.shortcuts import render
from django.http import HttpResponse
import databaseMethod
# Create your views here.


def index(request):
    data = databaseMethod.showDataBase()
    my_data = {'data': data}
    return render(request, 'first_app/index.html', context=my_data)


def indexOne(request):
    return render(request, 'first_app/indexOne.html', {'data': '<h1>Hello</h1>'})


def indexTwo(request):
    return HttpResponse("Second App")
