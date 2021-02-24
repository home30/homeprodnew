from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', views.index, name='index'),
    path('team/',views.expertteam, name='team'),
    path('ourpackages/',views.packages,name='packages'),
    path('landlords/',views.landlords, name='landlords'),
    path('modal/',views.modal,name='modal'),
    path('auction/',views.auction,name='auction'),
    path('management/',views.management,name='management'),
    path('contact/',views.contact,name='contact'),
    path('privacy-policy-and-notice/',views.privacy,name='privacy'),
    path('Cookie-Policy',views.cookie,name='cookie')
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)