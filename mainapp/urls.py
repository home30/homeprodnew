from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('team/',views.expertteam, name='team'),
    path('ourpackages/',views.packages,name='packages'),
    path('landlords/',views.landlords, name='landlords'),
    path('modal/',views.modal,name='modal'),
]