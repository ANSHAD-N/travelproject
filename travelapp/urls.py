from . import views
from django.urls import path

app_name = "travelapp"

urlpatterns = [
    path('', views.demo, name='demo'),
    path('add/', views.addition, name='add'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts')

]
