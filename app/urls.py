from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('he-thong/', views.pharmacy_system, name='pharmacy_system'), 
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-dashboard/add/', views.medicine_add, name='medicine_add'),
    path('admin-dashboard/edit/<int:pk>/', views.medicine_edit, name='medicine_edit'),
    path('admin-dashboard/delete/<int:pk>/', views.medicine_delete, name='medicine_delete'),
]

# Thêm dòng này để xem được ảnh đã upload
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)