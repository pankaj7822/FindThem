from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from FindThem.forms import SignUpForm, SearchForm
from django.contrib.auth.models import User

def home(request):
    return render(request, "home.html", {'title': "Home"})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form, 'title': 'Signup'})

def search(request):

    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            pass
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form, 'title': 'Search'})

