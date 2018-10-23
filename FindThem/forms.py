from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Person, Disaster


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class SearchForm(forms.ModelForm):
    alive = forms.BooleanField(widget = forms.HiddenInput(), initial=True)
    class Meta:
        model = Person
        fields = '__all__'