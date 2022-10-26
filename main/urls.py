from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('Главная.html', views.glav, name='Главная.html'),
    path('about.html', views.about, name='about.html'),
    path('Store.html', views.Store, name='Store.html'),
    path('YUMMS.html', views.YUMMS, name='YUMMS.html')
]
