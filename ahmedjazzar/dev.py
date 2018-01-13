from .common import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ahmedjazzar',
        'USER': 'root',
    },
}

SITE_BASE = 'http://127.0.0.1'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '.compiled', 'mediafiles')
