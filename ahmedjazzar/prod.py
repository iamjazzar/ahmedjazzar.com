
from .base import *

DEBUG = False
TEMPLATE_DEBUG = False
IS_LIVE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': '5432',
    }
}


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow ahmedjazzar.herokuapp.com headers
ALLOWED_HOSTS = ['ahmedjazzar.herokuapp.com']

# Static and Media asset configuration

# AWS_STORAGE_BUCKET_NAME = "<BUCKET_NAME_GOES_HERE>"
# AWS_ACCESS_KEY_ID = "<ACCESS_KEY_ID_GOES_HERE>"
# AWS_SECRET_ACCESS_KEY = "<SECRET_ACCESS_KEY_GOES_HERE>"

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'


STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '.compiled'),
)
