
from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DEV_DB_NAME,
        'USER': DEV_DB_USER,
        'PASSWORD': DEV_DB_PASSWORD,
        'HOST': 'db',
        'PORT': 5432,
    },
}



STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static', 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '.compiled'),
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static', 'mediafiles')
