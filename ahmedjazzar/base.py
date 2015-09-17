
# NOTE: Uncomment vars then add your own secret vars OR keep them commented and
# declare them in secret_vars.py. You also need to look up ahmedjazzar and
# ahmedjazzarcom in the entire project and change them to settings_folder_name
# and app_name respectively

import os

from .secret_vars import *


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECRET_KEY = "<Y0uR-4pP_$ecRe7_K3y:)>"

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'twitter_text',
    'storages',
    'ahmedjazzarcom',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'ahmedjazzar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'ahmedjazzar.wsgi.application'

# Personal vars

TWITTER_USERNAME = 'AhmedAljazzar'
GITHUB_USERNAME = 'ahmedaljazzar'
EMAIL = 'ahmed.mojaz@gmail.com'

# twitter settings

# CONSUMER_KEY='[your consumer key]'
# CONSUMER_SECRET='[your consumer secret]'
# ACCESS_TOKEN='[your token]'
# ACCESS_TOKEN_SECRET='[your token secret]'


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
