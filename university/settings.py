import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')!@hiilxvfi-)&b^(sead9g2jm3$5+-sd&ma^$+6hvlpjdd@!y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Modulos.Academica',
    'crispy_forms',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'University.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['C:/Users/elkin/OneDrive/Escritorio/Elkin/2022-2/Arquitecura de Software/Trabajos/university/Modulos/Academica/plantillas'],
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

WSGI_APPLICATION = 'University.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'University.db',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-col'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

#EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
#EMAIL_HOST = "smtp.gmail.com"
#EMAIL_USE_TLS = True
#EMAIL_PORT = 587
#EMAIL_HOST_USER = "mensajeriamintic2022@gmail.com"
#EMAIL_HOST_PASSWORD = "misiontic2022"

#EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
#EMAIL_HOST = "smtp.mailtrap.io"
#EMAIL_USE_TLS = True
#EMAIL_PORT = 587
#EMAIL_HOST_USER = "94d2b2a857d50e"
#EMAIL_HOST_PASSWORD = "149860c61496bb"



#EMAIL_HOST = 'smtp.mailtrap.io'
#EMAIL_HOST_USER = '94d2b2a857d50e'
#EMAIL_HOST_PASSWORD = '149860c61496bb'
#EMAIL_PORT = '2525'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_TMP = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

os.makedirs(STATIC_TMP, exist_ok=True)
os.makedirs(STATIC_ROOT, exist_ok=True)

STATICFILES_DIRS = (os.path.join(BASE_DIR, '')
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'