"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hg#)4=o_^wc*aeobn(gqkaxd#i%e+pmm$zzg%c*-=)dk2m1&7y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# User Registration and Login
AUTHENTICATION_BACKENDS = (
    # Django-side login
    'django.contrib.auth.backends.ModelBackend',
    # All-auth-side login
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Set Maximum File Download Size
DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760

# Application definition

INSTALLED_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'chartjs',
    # 'django_plotly_dash.apps.DjangoPlotlyDashConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'whatsanalyzer.apps.WhatsanalyzerConfig',
]

# Django allauth settings
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 10
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 30             # seconds
ACCOUNT_LOGOUT_REDIRECT_URL ='/'
LOGIN_REDIRECT_URL = '/'
SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Singapore'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'

'''
1. Specify the STATICFILES_DIR. Best practice is to create a folder
named static in your root directory (in the same folder as your manage.py
file), and place all static content (css, js, img, etc) there

2. Specify the DJANGO STATIC_ROOT DIRECTORY. This is the folder where
Django LOOKS AT DURING RUNTIME (optimized for speed/convenience) to 
obtain all its static assets --> this folder is the 'assets' folder in the root dir

3. This STATIC_ROOT directory is initially non-existent. You've to do
python manage.py collectstatic in the directory containing both manage.py
and your created static folder in Step 1 to TRANSFER ALL FILES from 'static' 
folder to the 'assets' folder

4. Once that is done, we need to ALTER THE HTML FILE LINKS to these
static files

Before : <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet">
After  : <link href="{% static 'vendor/fontawesome-free/css/all.min.css' %}" rel="stylesheet">

We've to encapsulate the absolute link in SINGLE-QUOTES, and then WRAP
{% '<ORIGINAL/ABSOLUTE/LINKS' %} in THESE % BRACKETS
'''

# Step 1
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    #'/var/www/static/', # for hardcoded URLs
]
# Step 2
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

# Step 3
# In terminal (python manage.py collectstatic)

# Step 4
# Alter HTML links in <file_name>.html


# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}