from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('english', views.english_course),
    path('french', views.french_course),
    path('spanish', views.spanish_course),
    path('portfolio', views.portfolio),
    path('about', views.about_project),
    path('contacts', views.contacts),
    path('faq', views.faq)
]
