from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CitiesForm
from .models import Cities


# Create your views here.
def index(request):
    return render(request, 'widgetApp/index.html')


def applyPage(request):
    if request.method == "POST":
        form_cities = CitiesForm(request.POST)
        if form_cities.is_valid():
            form_cities.save()
            print(request.POST)
            return redirect("confirmPage")
        else:
            print("INVALID")
            print(form_cities.errors)
    return render(request, 'widgetApp/applyPage.html', {'form': CitiesForm()})


def confirmPage(request):
    city = Cities.objects.all()
    return render(request, 'widgetApp/confirmPage.html', {'city': city})
