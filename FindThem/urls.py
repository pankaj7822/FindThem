from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),    
    path('accounts/signup/', views.signup, name="signup"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('search/', views.search, name="search")
]
