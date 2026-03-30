from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Medicine, MedicineImage, Pharmacy  # Đã thêm Pharmacy vào đây

# 1. Trang chủ dành cho khách hàng
def home(request):
    query = request.GET.get('q', '').strip()
    if query:
        medicines = Medicine.objects.filter(name__icontains=query)
    else:
        medicines = Medicine.objects.all()
    return render(request, 'app/home.html', {'medicines': medicines, 'query': query})

# 2. Quản trị Dashboard chính - Xử lý hiển thị thuốc VÀ cửa hàng
def admin_dashboard(request):
    medicines = Medicine.objects.all()
    # QUAN TRỌNG: Phải lấy danh sách cửa hàng ra để hiển thị
    pharmacies = Pharmacy.objects.all() 
    
    # Logic xử lý khi nhấn "LƯU THÔNG TIN CỬA HÀNG"
    if request.method == "POST":
        store_name = request.POST.get('store_name')
        if store_name: 
            address = request.POST.get('address')
            lat = request.POST.get('lat')
            lon = request.POST.get('lon')
            
            if lat and lon:
                Pharmacy.objects.create(
                    name=store_name,
                    address=address,
                    location_lat=float(lat),
                    location_lon=float(lon),
                    phone="0123456789" 
                )
                messages.success(request, f"Đã thêm chi nhánh {store_name} thành công!")
                return redirect('admin_dashboard')
            else:
                messages.error(request, "Vui lòng chọn vị trí trên bản đồ hoặc nhập tọa độ!")

    # Gửi cả 'medicines' và 'pharmacies' sang template
    return render(request, 'dashboard/index.html', {
        'medicines': medicines, 
        'pharmacies': pharmacies
    })

# 3. Hệ thống nhà thuốc (trang xem bản đồ của khách)
def pharmacy_system(request):
    # Lấy toàn bộ danh sách nhà thuốc từ database
    pharmacies_list = Pharmacy.objects.all()
    
    return render(request, 'app/pharmacy_system.html', {
        'pharmacies': pharmacies_list # Biến này sẽ được dùng trong HTML
    })

# 4. Thêm sản phẩm mới (Xử lý lỗi giá tiền rỗng)
def medicine_add(request):
    if request.method == "POST":
        price_raw = request.POST.get('price')
        try:
            # Chuyển đổi giá tiền an toàn, nếu rỗng thì mặc định là 0
            price = float(price_raw) if price_raw else 0
            
            medicine = Medicine.objects.create(
                name=request.POST.get('name'),
                category=request.POST.get('category'),
                unit=request.POST.get('unit'),
                price=price
            )
            
            images = request.FILES.getlist('images')
            for img in images:
                MedicineImage.objects.create(medicine=medicine, image=img)
                
            messages.success(request, "Thêm sản phẩm thành công!")
            return redirect('admin_dashboard')
        except ValueError:
            messages.error(request, "Giá tiền không hợp lệ!")
        
    return render(request, 'dashboard/add.html')

# 5. Sửa sản phẩm
def medicine_edit(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == "POST":
        price_raw = request.POST.get('price')
        try:
            medicine.name = request.POST.get('name')
            medicine.category = request.POST.get('category')
            medicine.unit = request.POST.get('unit')
            medicine.price = float(price_raw) if price_raw else 0
            medicine.save()

            images = request.FILES.getlist('images')
            if images:
                for img in images:
                    MedicineImage.objects.create(medicine=medicine, image=img)

            messages.success(request, "Cập nhật thành công!")
            return redirect('admin_dashboard')
        except ValueError:
            messages.error(request, "Giá tiền không hợp lệ!")
        
    return render(request, 'dashboard/edit.html', {'medicine': medicine})

# 6. Xóa sản phẩm
def medicine_delete(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == "POST":
        medicine.delete()
        messages.warning(request, "Đã xóa sản phẩm.")
        return redirect('admin_dashboard')
    return render(request, 'dashboard/delete.html', {'medicine': medicine})

# 7. Auth (Giữ nguyên của bạn)
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('admin_dashboard' if user.is_staff else 'home')
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

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

def login_success(request):
    return render(request, 'app/login_success.html')

def cart_view(request):
    # Thêm 'app/' vào trước tên file
    return render(request, 'app/cart.html')

def product_detail(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    # Hãy đảm bảo có 'app/' ở phía trước nếu file nằm trong templates/app/
    return render(request, 'app/product_detail.html', {'medicine': medicine})