from django.urls import path
from . import views

urlpatterns=[
    path('', views.charging_page, name='charging_page'),
    path('index/', views.index, name='index'),
    path('social/', views.social, name='social'),
    path('conseil/', views.conseil, name='conseil'),

]