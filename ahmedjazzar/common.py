import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = os.environ.get('SECRET_KEY', 'Dev)loPmen7K3y')

ALLOWED_HOSTS = []
SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'robots',
    'markdown_deux',
    'martor',
    'meta',
    'secretballot',
    'storages',

    'ahmedjazzarcom.apps.AhmedjazzarcomConfig',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'secretballot.middleware.SecretBallotIpUseragentMiddleware',
]


ROOT_URLCONF = 'ahmedjazzar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'ahmedjazzar.context_processors.ahmedjazzar',
            ],
        },
    },
]

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '.compiled'),
    os.path.join(BASE_DIR, 'static'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'


MARTOR_UPLOAD_PATH = 'uploads/posts'
MARTOR_UPLOAD_URL = '/api/upload/'
MAX_IMAGE_UPLOAD_SIZE = 5242880
MARTOR_MARKDOWN_SAFE_MODE = False # default

WSGI_APPLICATION = 'ahmedjazzar.wsgi.application'

# google Analytics
GOOGLE_TRACKING_KEY = 'UA-46039118-3'

# Internationalization

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
