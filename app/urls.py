from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('he-thong/', views.pharmacy_system, name='pharmacy_system'),
]