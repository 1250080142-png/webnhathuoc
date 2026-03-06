from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Medicine, Pharmacy

def home(request):
    # Lấy danh sách thuốc đổ ra trang chủ
    medicines = Medicine.objects.all().order_by('-id')[:8] 
    return render(request, 'app/home.html', {'medicines': medicines})

def pharmacy_system(request):
    pharmacies = Pharmacy.objects.all()
    return render(request, 'app/pharmacy_system.html', {'pharmacies': pharmacies})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})

@login_required
def login_success(request):
    """Điều hướng người dùng sau khi đăng nhập thành công để tránh lỗi 404"""
    if request.user.is_staff or request.user.is_superuser:
        return redirect('dashboard_home')
    return redirect('home')