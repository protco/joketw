import os
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['JT_DB_NAME'],
        'USER': os.environ['JT_DB_USER'],
        'PASSWORD': os.environ['JT_DB_PWD'],
        'HOST': '',
        'PORT': '',
    }
}
import dj_database_url
DATABASES = { 'default': dj_database_url.config() }

