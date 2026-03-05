from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Medicine, Pharmacy

def home(request):
    medicines = Medicine.objects.all().order_by('-id')[:8] 
    return render(request, 'app/home.html', {'medicines': medicines})

def pharmacy_system(request):
    pharmacies = Pharmacy.objects.all()
    return render(request, 'app/pharmacy_system.html', {'pharmacies': pharmacies})

def register(request):
    """Hàm xử lý đăng ký tài khoản khách hàng"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Đăng ký xong cho đăng nhập luôn
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})

@login_required
def login_success(request):
    """Hàm kiểm tra: Nếu là Admin/Staff thì vào Dashboard, nếu là Khách thì về trang chủ"""
    if request.user.is_staff or request.user.is_superuser:
        return redirect('dashboard_home')
    return redirect('home')