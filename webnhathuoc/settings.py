from pathlib import Path
import os

# --- 1. CẤU HÌNH ĐƯỜNG DẪN CƠ BẢN ---
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "django-insecure-unv3^8u-9-b7s82(4h$&&y_%xf@ekrxwyr=@ha&)hsvg$+ydxo"
DEBUG = True
ALLOWED_HOSTS = []

# --- 2. DANH SÁCH ỨNG DỤNG ---
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize", # Hỗ trợ định dạng số (1.000.000đ)
    "app",        # App chính (Trang chủ, Thuốc)
    "dashboard",  # App quản trị tự chế
]

# --- 3. CÁC LỚP TRUNG GIAN (MIDDLEWARE) ---
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "webnhathuoc.urls"

# --- 4. CẤU HÌNH GIAO DIỆN (TEMPLATES) ---
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')], # Thêm thư mục templates chung nếu có
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "webnhathuoc.wsgi.application"

# --- 5. CƠ SỞ DỮ LIỆU ---
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# --- 6. KIỂM TRA MẬT KHẨU ---
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --- 7. NGÔN NGỮ VÀ THỜI GIAN ---
LANGUAGE_CODE = "vi" # Đổi sang tiếng Việt cho thân thiện
TIME_ZONE = "Asia/Ho_Chi_Minh" # Đổi sang múi giờ Việt Nam
USE_I18N = True
USE_TZ = True

# --- 8. CẤU HÌNH FILE TĨNH VÀ MEDIA ---
STATIC_URL = "static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] # Thư mục chứa CSS, JS của bạn

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # Nơi lưu ảnh thuốc bạn tải lên

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --- 9. QUAN TRỌNG: CẤU HÌNH ĐIỀU HƯỚNG ĐĂNG NHẬP ---
# Sau khi đăng nhập xong, nhảy vào hàm login_success để phân luồng (Admin/Khách)
LOGIN_REDIRECT_URL = 'login_success'

# Sau khi đăng xuất, quay về trang chủ
LOGOUT_REDIRECT_URL = 'home'

# Trang để đăng nhập
LOGIN_URL = 'login'