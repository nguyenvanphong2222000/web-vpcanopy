"""Defines URL patterns for users"""
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
    # Login page
    path('login/', LoginView.as_view(template_name= 'users/login.html'), name='login'),
    # Logout page
    path('logout/', views.logout_view, name='logout'),
    # Registration page
    path('register/', views.register, name='register'),
    # Profile
    path('profile/', views.profile, name='profile'),
]