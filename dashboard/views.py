from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from app.models import Medicine 

@staff_member_required(login_url='login') # Chỉ cho phép nhân viên vào, nếu chưa login sẽ đẩy ra trang login
def dashboard_index(request):
    medicines = Medicine.objects.all() 
    return render(request, 'dashboard/index.html', {'medicines': medicines})