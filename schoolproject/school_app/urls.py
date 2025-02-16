from django.urls import path
from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('guide/', views.home, name='home'),        # Home Page
    path('', views.guide, name='guide'),  # Guide/Login Page
    path('register/', views.register, name='register'),
    path('profile/',views.profile,name='profile'),
    path('about/', views.about, name='about'),  # About Page
    path('contact/', views.contact, name='contact'),  # Contact Page
    path('terms/', views.terms, name='terms'),
    path('work/', views.work, name='work'), 
    path('plans/', views.plans, name='plans'), # Terms & Conditions Page
]
