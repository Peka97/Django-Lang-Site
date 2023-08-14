from typing import Any, Dict
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy
from django.http.request import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


# class LoginUserView(SingleObjectMixin, LoginView):
#     object = None
#     template_name = 'users/auth.html'
#     success_url = reverse_lazy('')

#     def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         return context

#     def get_success_url(self) -> str:
#         return reverse_lazy('')


def user_auth(request):
    context = {}

    if request.POST:
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'main/index.html', context)

        context = {'error': 'Username or password not correct'}

    return render(request, 'users/auth.html', context)


def user_logout(request):
    logout(request)
    return redirect('')


def user_profile(request):
    context = {}
    return render(request, '<h1>Profile page</h1>', context)
