from django.shortcuts import render
from .models import Appak
# Create your views here.
from django.http import HttpResponse


def index(request):
    appguztik = Appak.objects.all();
    return render(request, "lista_atara.html", {'appguztik':appguztik})

