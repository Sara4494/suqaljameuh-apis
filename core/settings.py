
from datetime import timedelta
from celery.schedules import crontab
from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _


#from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-97s7v(4cjlcf@dt2q+i0dcmqx*myg)0h#2o4%=)mjx(a+b15j&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = [
    "*"
]


# Application definition

INSTALLED_APPS = [
    "modeltranslation",
    'daphne',
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'polymorphic',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "corsheaders",
    'varieties',
    'users',
    'Ad',
    'notification',
    'reports',
    'user_profile',
    'rest_framework',
    'rest_framework_simplejwt',
    'celery',
    'newsletter',
    'memberships',
    "menfashion",
    "django_celery_beat",
    "education",
    "motorbikes",
    "electronics",
    "computers",
    'comments',
    "cars",
    "apartments",
    'Analytics',
    'chat',
    'jobs',
    'settings',
    'ckeditor'
]


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',



]


ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'
ASGI_APPLICATION = "core.asgi.application"


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis://default:bOoFaHJgLpAkLGnk6ij4da3GAk53mJ12@roundhouse.proxy.rlwy.net:34842")],
        },
    },
}


AUTH_USER_MODEL = "users.User"


 

CORS_ALLOWED_ORIGINS = [
    "https://suqaljameuh.vercel.app",
    "https://suqeljumeh-dashboard.vercel.app"
]
ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = False

# Allow websites:
"""

"""

CSRF_TRUSTED_ORIGINS = [
    'https://suqaljameuh-apis.up.railway.app'
]


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
 
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
 
    }
}
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": "db.sqlite3",
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

LANGUAGE_CODE = 'en-ar'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# In this code, the above categorized news is scheduled to be sent every Monday, using the crontab function of celery.schedules.
# CELERY_BEAT_SCHEDULE = {
#     'send_top_rated_news': {
#         'task': 'newsletter.tasks.send_top_rated_news',
#         'schedule': crontab(day_of_week='monday'),


#         'check_user_memberships': {
#             'task': 'memberships.tasks.check_user_memberships',
#             'schedule': timedelta(days=1),
#         },
#         'check_featured_memberships': {
#             'task': 'memberships.tasks.check_featured_memberships',
#             'schedule': timedelta(days=1),
#         },
#     }}


STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "staticfiles")]
STATIC_ROOT = os.path.join(BASE_DIR, "static")

AUTH_USER_MODEL = 'users.User'

STRIPE_PUBLIC_KEY = os.environ.get("STRIPE_PUBLIC_KEY")
STRIPE_PRIVATE_KEY = os.environ.get("STRIPE_PRIVATE_KEY")


CELERY_BROKER_URL = (
    "redis://default:bOoFaHJgLpAkLGnk6ij4da3GAk53mJ12@roundhouse.proxy.rlwy.net:34842"
)
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_TIMEZONE = "Africa/Cairo"
# Asia/Riyadh

# CELERY BEAT
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"


# rest framework settings

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "EXCEPTION_HANDLER": "globals.exception_handler.custom_exception_handler",
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=90),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
}

# CELERY BEAT


# Available Languages
LANGUAGES = [
    ('en', _('English')),
    ('ar', _('Arabic')),
]

# Locales available path
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
 


#! PAYMENTS-SPECIFIC INFO, DON"T TOUCH IT AT ALL!!
STRIPE_PUBLIC_KEY = os.environ.get("STRIPE_PUBLIC_KEY")
STRIPE_PRIVATE_KEY = os.environ.get("STRIPE_PRIVATE_KEY")
PAYPAL_CLIENT_ID = os.environ.get("PAYPAL_CLIENT_ID")
PAYPAL_SECRET_KEY = os.environ.get("PAYPAL_SECRET_KEY")

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "yosofaymanessawy@gmail.com"
EMAIL_HOST_PASSWORD = "ylic uvwl algc jyfl"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
 