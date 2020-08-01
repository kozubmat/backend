from django.shortcuts import render, redirect
from fleet.models import Car, PETROL_CHOICES, Company
# Create your views here.

def car_list(requests):
    cars = list(Car.objects.all())
    return render(requests, "car_list.html",{
        "cars": cars
    })

def car_form(requests, pk=0):

    car = None
    if int (pk or 0):
        car = Car.objects.get(pk=pk)

    if requests.method == "POST":
        if not car:
            Car.objects.create(
                brand=requests.POST['brand'],
                model=requests.POST['model'],
                year=requests.POST['year'],
                petrol=requests.POST['petrol'],
                owner=requests.POST['owner']
            )
        else:
            car.brand = requests.POST['brand']
            car.model = requests.POST['model']
            car.year = requests.POST['year']
            car.petrol = requests.POST['petrol']
            car.owner_id = requests.POST['owner']
            car.save()

        return redirect(car_list)


    return render(requests, "car_form.html", {
        "PETROL_CHOICES": PETROL_CHOICES,
        "car": car,
        "company": Company.objects.all()

    })