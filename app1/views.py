from django.shortcuts import render,HttpResponse
from .models import Car
def viewCars(request) :
    car_dict={'cars': Car.objects.all()}
    print(Car.objects.all().order_by('model'))
    return render(request,'app1/index.html',car_dict)
