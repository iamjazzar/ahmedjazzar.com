from .common import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ahmedjazzar',
    },
}



STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static', 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '.compiled'),
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '.compiled', 'mediafiles')
