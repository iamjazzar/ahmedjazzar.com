from .common import *

DEBUG = False
TEMPLATE_DEBUG = False
IS_LIVE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
    }
}


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow ahmedjazzar.herokuapp.com headers
ALLOWED_HOSTS = [
'ahmedjazzar.herokuapp.com',
'.ahmedjazzar.com',
'.ahmedjazzar.com.'
]

SITE_BASE = 'www.ahmedjazzar.com'


# Static and Media asset configuration
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

AWS_S3_CUSTOM_DOMAIN = 'd3ffm3ou81sw69.cloudfront.net'


STATIC_FILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATIC_FILES_LOCATION)

MEDIA_FILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIA_FILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

META_SITE_PROTOCOL = 'https'
META_SITE_DOMAIN = 'www.ahmedjazzar.com'
