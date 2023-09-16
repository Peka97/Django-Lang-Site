from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('<int:id>/<int:step>', views.exercises_words, name='exercises_words'),
    path('update', views.update, name='update')
]
