from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('he-thong/', views.pharmacy_system, name='pharmacy_system'),
    path('register/', views.register, name='register'),
    path('login-success/', views.login_success, name='login_success'),
]