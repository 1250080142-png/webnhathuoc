from django.urls import path
from . import views

urlpatterns = [
    # Đây là trang chủ của dashboard (ví dụ: http://127.0.0.1:8000/dashboard/)
    path('', views.dashboard_index, name='dashboard_home'),
]