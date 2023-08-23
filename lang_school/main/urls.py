from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('english', views.english_course, name='english'),
    path('french', views.french_course, name='french'),
    path('spanish', views.spanish_course, name='spanish'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('about', views.about_project, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('faq', views.faq, name='faq')
]
