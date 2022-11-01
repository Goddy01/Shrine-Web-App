"""
Django settings for shrineApp project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os, dj_database_url
from dotenv import load_dotenv, find_dotenv
from django.contrib import messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(find_dotenv())

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['oduduwashrine.up.railway.app']
CSRF_TRUSTED_ORIGINS=['oduduwashrine.up.railway.app', ]

# Application definition

INSTALLED_APPS = [
    'accounts',
    'donations',
    'events',
    'sermons',
    'shrine',
    'news',
    'phonenumber_field',
    'phonenumbers',
    'ckeditor',
    'django_countries',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
]

MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
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

ROOT_URLCONF = 'shrineApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'shrineApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'Shrine Web App DB',
            'USER': 'postgres',
            # 'PASSWORD': os.environ.get('POSTGRESQL_PASSWORD'),
            'PASSWORD': 'Qwerty121@',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
else:
    DATABASES = {
    'default': dj_database_url.config(default=f"postgresql://{os.environ.get('PGUSER')}:{os.environ.get('PGPASSWORD')}@{os.environ.get('PGHOST')}:{os.environ.get('PGPORT')}/{os.environ.get('PGDATABASE')}", conn_max_age=600)
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.ScryptPasswordHasher',
]

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

AUTH_USER_MODEL = 'accounts.UserProfile'
# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CKEDITOR CONFIGURATIONS
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 'full',
    },
}
# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': [
#             ['Undo', 'Redo',
#              '-', 'Bold', 'Italic', 'Underline',
#              '-', 'Link', 'Unlink', 'Anchor',
#              '-', 'Format',
             
#              '-', 'Maximize',
             
#             ],
#         ],  
#         'height': 300,
#         'width': 'auto',
#         'toolbarCanCollapse': True,
#     },
# }
# Sending mails
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'bloggie.blogapp@gmail.com'
EMAIL_HOST_PASSWORD = 'pktwaipegwuzmigr'
DEFAULT_FROM_EMAIL = 'Oduduwa Shrine Team <noreply@oduduwa.com>'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


# AWS CONFIGURATION
if not DEBUG:
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_DEFAULT_ACL = 'public-read'

    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400'
    }

    AWS_LOCATION = 'static'
    AWS_QUERYSTRING_AUTH = False
    AWS_HEADERS = {
        'Access-Control-Allow-Origin': '*',
    }

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    # STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

    COLLECTFAST_STRATEGY = "collectfast.strategies.boto3.Boto3Strategy"
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
    DEBUG_PROPAGATE_EXCEPTIONS = True


# TO PREVENT 400 ERROR
LOGGING = {
'version': 1,
'disable_existing_loggers': False,
'formatters': {
    'verbose': {
        'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
        'datefmt' : "%d/%b/%Y %H:%M:%S"
    },
    'simple': {
        'format': '%(levelname)s %(message)s'
    },
},
'handlers': {
    'file': {
        'level': 'DEBUG',
        'class': 'logging.FileHandler',
        'filename': 'mysite.log',
        'formatter': 'verbose'
    },
},
'loggers': {
    'django': {
        'handlers':['file'],
        'propagate': True,
        'level':'DEBUG',
    },
    'MYAPP': {
        'handlers': ['file'],
        'level': 'DEBUG',
    },
}
}