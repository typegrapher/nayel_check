from pathlib import Path
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = ["*"]




# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web',
    'versatileimagefield',
    'tinymce',
]

TINYMCE_DEFAULT_CONFIG = {
    'height': '45vh',
    'width': '100%',
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
                "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
                "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
                "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
                "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
                "a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10,
}
TINYMCE_SPELLCHECKER = False
TINYMCE_FILEBROWSER = True


# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'kfaamardesubombhack@gmail.com'
EMAIL_HOST_PASSWORD = 'ggzzuxirzwivxefi'
# DEFAULT_FROM_EMAIL = 'kfaamardesubombhack@gmail.com'
EMAIL_USE_TLS = True



VERSATILEIMAGEFIELD_SETTINGS = {
	'cache_length': 2592000,
	'cache_name': 'versatileimagefield_cache',
	'jpeg_resize_quality': 70,
	'sized_directory_name': '__sized__',
	'filtered_directory_name': '__filtered__',
	'placeholder_directory_name': '__placeholder__',
	'create_images_on_demand': True,
	'image_key_post_processor': None,
	'progressive_jpeg': False
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nayel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'nayel.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": config("DB_ENGINE", default="django.db.backends.sqlite3"),
#         "NAME": config("DB_NAME", default=BASE_DIR / "db.sqlite3"),
#         "USER": config("DB_USER", default=""),
#         "PASSWORD": config("DB_PASSWORD", default=""),
#         "HOST": config("DB_HOST", default="localhost"),
#         "PORT": "",
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
STATIC_URL = "/static/"
STATIC_FILE_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = ((BASE_DIR / "static"),)
STATIC_ROOT = BASE_DIR / "assets"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
