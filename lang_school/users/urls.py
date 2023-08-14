from django.urls import path, include
from . import views

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('auth', views.user_auth, name='auth'),
    path('profile', views.user_profile, name='profile'),
    path('logout', views.user_logout, name='logout')
]
