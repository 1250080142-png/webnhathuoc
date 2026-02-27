from django.shortcuts import render
from .models import Medicine, Pharmacy

def home(request):
    # Lấy 8 thuốc mới nhất để hiển thị trang chủ
    medicines = Medicine.objects.all().order_by('-id')[:8] 
    return render(request, 'app/home.html', {'medicines': medicines})

def pharmacy_system(request):
    # Lấy danh sách nhà thuốc cho bản đồ GIS
    pharmacies = Pharmacy.objects.all()
    return render(request, 'app/pharmacy_system.html', {'pharmacies': pharmacies})