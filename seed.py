import os
import django

# Thiết lập môi trường Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webnhathuoc.settings')
django.setup()

from app.models import Medicine

# Dữ liệu mẫu giống hình Long Châu
medicines_data = [
    {
        "name": "Cốm vi sinh bổ sung lợi khuẩn Lacto Biomin Gold+",
        "category": "Thực phẩm chức năng",
        "price": 119200,
        "image_url": "https://nhathuoclongchau.com.vn/images/product/2023/01/00502124-com-vi-sinh-lacto-biomin-gold-bo-sung-loi-khuan-duong-ruot-20-goi-x-3g-6354-63bd_large.jpg",
        "unit": "Hộp",
    },
    {
        "name": "Viên uống bổ gan hỗ trợ tăng cường chức năng gan Kanzo Gold",
        "category": "Thực phẩm chức năng",
        "price": 960000,
        "image_url": "https://nhathuoclongchau.com.vn/images/product/2022/10/00030644-vien-uong-kanzo-gold-60v-tang-cuong-chuc-nang-gan-4328-6350_large.jpg",
        "unit": "Hộp",
    },
    {
        "name": "Dung dịch hỗ trợ phát triển xương, răng cho trẻ D3 Drops",
        "category": "Mẹ và Bé",
        "price": 270000,
        "image_url": "https://nhathuoclongchau.com.vn/images/product/2021/07/00023247-dung-dich-dao-nordic-health-d3-drops-ho-tro-hap-thu-canxi-9804-60f1_large.jpg",
        "unit": "Chai",
    }
]

print("Đang xóa dữ liệu cũ...")
Medicine.objects.all().delete()

print("Đang thêm dữ liệu mới...")
for item in medicines_data:
    Medicine.objects.create(**item)

print("Xong rồi! Giờ bạn ra web F5 lại nhé.")