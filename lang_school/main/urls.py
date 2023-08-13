from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('english', views.english_course),
    path('french', views.french_course),
    path('spanish', views.spanish_course),
    path('portfolio', views.portfolio),
    path('about', views.about_project),
    path('contacts', views.contacts)
]
