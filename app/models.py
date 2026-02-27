from django.db import models
from django.contrib.auth.models import User

# --- 1. QUẢN LÝ NHÀ THUỐC & NHÂN SỰ ---
class Pharmacy(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    image_url = models.URLField(max_length=1000, null=True, blank=True)
    location_lat = models.FloatField(null=True, blank=True, help_text="Vĩ độ")
    location_lon = models.FloatField(null=True, blank=True, help_text="Kinh độ")
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class StaffProfile(models.Model):
    ROLE_CHOICES = [('ADMIN', 'Quản trị viên'), ('PHARMACIST', 'Dược sĩ'), ('CASHIER', 'Thu ngân')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# --- 2. QUẢN LÝ KHO ---
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image_url = models.URLField(max_length=1000, null=True, blank=True)
    unit = models.CharField(max_length=50, help_text="Vỉ, Hộp, Viên")
    min_stock_level = models.IntegerField(default=10)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    current_quantity = models.PositiveIntegerField(default=0)
    class Meta:
        unique_together = ('pharmacy', 'medicine')

# --- 3. QUẢN LÝ HÓA ĐƠN ---
class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, unique=True)
    points = models.IntegerField(default=0)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.full_name

class Invoice(models.Model):
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)