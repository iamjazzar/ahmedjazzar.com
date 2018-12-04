from .common import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'ahmedjazzar.sqlite3'),
    },
}

SITE_BASE = 'http://127.0.0.1'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '.compiled', 'mediafiles')

META_SITE_PROTOCOL = 'http'
META_SITE_DOMAIN = 'localhost'
