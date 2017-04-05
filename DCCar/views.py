from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from DCCar.forms import ReserveForm
from DCCar.models import Car


def index(request):
    cars = Car.objects.all()
    context = {
        'cars': cars
    }
    return render(request, 'DCCar/index.html', context)

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    context ={
        'car': car
    }
    return render(request, 'DCCar/car_details.html', context)


def reserve(request, car_id):
    car = Car.objects.get(id=car_id)
    if request.POST:
        form = ReserveForm(request.POST)
        print "hola"
        if form.is_valid():
            print "hola"
            form.save()
        else:
            return render(request, 'DCCar/reserve.html', {'car': car, 'form': form})
            
    form = ReserveForm(initial={'car': car})
    context = {
        'car': car,
        'form': form
    }
    return render(request, 'DCCar/reserve.html', context)

