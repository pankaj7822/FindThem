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

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            if form.status == "Missing" :
                result = Person.objects.filter(age__gt=form.age-5, age__lt=form.age+5, gender=form.gender, blood_group = form.blood_group, height__gt = form.height*0.8, height__lt = form.height*1.2, disaster = form.disaster )
            elif form.status == "Found":
                form.save()
            form = None
        else:
            print(form.errors)
    else:
        form = SearchForm()
        result = None

    return render(request, 'search.html', {'form': form, 'title': 'Search', 'result':result})
            
    