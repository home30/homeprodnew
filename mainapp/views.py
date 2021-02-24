from django.shortcuts import render
from .models import team


# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')


def expertteam(request):
    teams = team.objects.all()
    return render(request, 'mainapp/team.html', {'teams': teams})


def packages(request):
    return render(request, 'mainapp/ourpackages.html')


def landlords(request):
    return render(request, 'mainapp/landlords.html')


def modal(request):
    teams = team.objects.all()
    return render(request, 'mainapp/modal.html', {'teams': teams})


def auction(request):
    return render(request, 'mainapp/auction.html')


def management(request):
    return render(request, 'mainapp/management.html')

def contact(request):
    return render(request,'mainapp/contact.html')

def privacy(request):
    return render(request,'mainapp/privacy.html')

def cookie(request):
    return render(request,'mainapp/cookie.html')