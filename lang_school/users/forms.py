from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm

from users.models import *


class RegistrationUserForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            {'class': 'form-control'}
        ),
        label='Имя'
    )
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            {'class': 'form-control'}
        ),
        label='Фамилия'
    )

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(UserCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField()
