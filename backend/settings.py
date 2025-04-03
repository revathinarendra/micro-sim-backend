# settings.py

from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG') == 'False'
SITE_ID = 1

ALLOWED_HOSTS = ['.vercel.app', 'localhost', '127.0.0.1','*','microsim2.vercel.app', 'micro-sim-backend.vercel.app',]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    'phonenumber_field',
    'rest_framework',
    'corsheaders',
    'dj_rest_auth',
  	'dj_rest_auth.registration',
    'rest_framework.authtoken',

    # Allauth apps
    
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
]

OUR_APPS = [
    'accounts',
    'flashcard',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + OUR_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',

]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("SUPBASE_DB_NAME"),
        "USER": os.environ.get("SUPBASE_DB_USER"),
        "PASSWORD": os.environ.get("SUPBASE_DB_PASSWORD"),
        "HOST": os.environ.get("SUPBASE_DB_HOST"),
        "PORT": os.environ.get("SUPBASE_DB_PORT"),
    }
}
# import dj_database_url

# DATABASES = {
#     "default": dj_database_url.config(default=os.environ.get('POSTGRES_URL'))
# }

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

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'utils.custom_exception_handler.custom_exception_handler',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
}
ADMIN_SITE_HEADER = 'WIKITUBE ADMIN'
ADMIN_SITE_TITLE = 'WIKITUBE'
ADMIN_INDEX_TITLE = 'Welcome to WIKITUBE'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

CORS_ALLOWED_ORIGINS = [
    'https://wikitube-django-backend.vercel.app',
    'https://microsim2.vercel.app',
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'https://microsim.vercel.app',
    'https://micro-sim-backend.vercel.app'
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'

AUTHENTICATION_BACKENDS = [
    'backends.custom_authentication_backend.CustomEmailBackend',
   
    'django.contrib.auth.backends.ModelBackend',  # Keep the default backend
    "allauth.account.auth_backends.AuthenticationBackend", 
]
#ACCOUNT_SIGNUP_REDIRECT_URL = "/accounts/google/redirect/" 
ACCOUNT_SIGNUP_REDIRECT_URL = "https://microsim2.vercel.app/home"

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY"),
            "secret": os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET"),
        },
        "SCOPE": ["email"],
        'AUTH_PARAMS': {'access_type': 'online'},
        'METHOD': 'oauth2',
        'VERIFIED_EMAIL': True,
        "OAUTH_PKCE_ENABLED": True,
        "REDIRECT_URI": "https://micro-sim-backend.vercel.app/accounts/google/login/callback/",
    }
}
ACCOUNT_ADAPTER = "allauth.account.adapter.DefaultAccountAdapter"
ACCOUNT_ADAPTER = "backend.adapter.MyAccountAdapter"
SOCIALACCOUNT_ADAPTER = "backend.adapter.MySocialAccountAdapter"

ACCOUNT_LOGIN_METHODS = {"email"}
ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*", "password2*"]

# Social Auth settings
ACCOUNT_LOGOUT_ON_GET = True

ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_EMAIL_VERIFICATION = "none"
SOCIALACCOUNT_EMAIL_VERIFICATION = "none"
SOCIALACCOUNT_AUTO_SIGNUP = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
CSRF_COOKIE_NAME = "csrftoken"
# Session settings
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7  # 7 days
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Redirect URLs
LOGIN_REDIRECT_URL = "https://microsim2.vercel.app/home"
ACCOUNT_LOGOUT_REDIRECT_URL = "https://microsim.vercel.app"

# CSRF settings
CSRF_TRUSTED_ORIGINS = [
    'https://microsim2.vercel.app',
    'https://micro-sim-backend.vercel.app',
    'https://microsim.vercel.app'
]

#SOCIAL_AUTH_GOOGLE_REDIRECT_URI = "https://micro-sim-backend.vercel.app/accounts/google/login/callback/"



# Frontend URL
FRONTEND_URL = 'https://microsim2.vercel.app'

# Authentication settings
ACCOUNT_EMAIL_VERIFICATION = 'none'
SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'
SOCIALACCOUNT_AUTO_SIGNUP = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

# Security settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


# Additional settings
SOCIALACCOUNT_LOGIN_ON_GET = True


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = "backends.custom_email_backend.CustomEmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", 587))
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "your_default_email@gmail.com")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "your_default_password")
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS", "True") == "True"
DEFAULT_FROM_EMAIL ="nucleus.edu.info@gmail.com"
