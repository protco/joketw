"""
Django settings for joketwitter project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

ALLOWED_HOSTS = ["127.0.0.1", 'joketwitter.herokuapp.com', 'www.joketwitter.com',  'joketwitter.com',]

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = os.environ['SECRET_KEY']
ADSENSE_ID = os.environ['ADSENSE_ID']
GOOGLE_ANALYTHICS_ID = os.environ['GOOGLE_ANALYTHICS_ID']

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'jokes',
    'star_ratings',

    # allauth:
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'userprofiles',
    'avatar',
    'bootstrap3',
    'bootstrapform',
    'django_extensions',
    'allauth.socialaccount.providers.google',
   # 'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',

    #restframework
    'rest_framework',
    #contact
    'envelope',
    # user relationship
    'friendship',
    #full site login_required
    'stronghold',
]
SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'stronghold.middleware.LoginRequiredMiddleware',

]

ROOT_URLCONF = 'joketwitter.urls'
LOGIN_REDIRECT_URL = '/userprofiles'
LOGOUT_URL = "/"

#ACCOUNT_EMAIL_REQUIRED (=True)
#ACCOUNT_EMAIL_VERIFICATION =”mandatory”

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates')],
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


AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'PAGE_SIZE': 10
}


WSGI_APPLICATION = 'joketwitter.wsgi.application'

#settings for star rating
STAR_RATINGS_RERATE = False
STAR_RATINGS_RANGE = 5
STAR_RATINGS_ANONYMOUS = False
STAR_RATINGS_RERATE = False
STAR_RATINGS_STAR_HEIGHT = 14
STAR_RATINGS_STAR_WIDTH  =14



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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
#STATIC_URL = '/static/'
# will not be served
#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static-storage'),]
#will be served
#STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static-serve')
#######################

#####heroku whitenoise
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static-storage"),)
STATIC_ROOT = os.path.join(BASE_DIR, "live-static-files", "static-root")
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "live-static-files", "media-root")

#email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'joketwittercom@gmail.com' #my gmail username
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD'] #my gmail password
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "Joke <joketwittercom@gmail.com>"

ADMINS = [('joke', EMAIL_HOST_USER)]
MANAGERS = ADMINS

#logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'mysite.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'MYAPP': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}
