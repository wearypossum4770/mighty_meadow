from os import getenv
from pathlib import Path

from dotenv import find_dotenv, load_dotenv

# =================================================================================
# SETUP FILES
# =================================================================================
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(find_dotenv())
DEBUG = getenv("DEBUG", True)
SECRET_KEY = getenv("SECRET_KEY", "abcdefg12345678")
ALLOWED_HOSTS = []
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# =================================================================================
# ADMINISTRATIVE
# =================================================================================
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = getenv("EMAIL_USER")
EMAIL_HOST_PASSWORD = getenv("EMAIL_PASS")
# =================================================================================
# APPLICATION
# =================================================================================
# Application definition
THIRD_PARTY_APPS = (
    "djoser",
    "channels",
    "whitenoise",
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "crispy_forms",
)
DEVELOPMENT_APPS = (
    "whitenoise.runserver_nostatic",
    "django_extensions",
)
PROJECT_APPS = ()
DJANGO_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
)
INSTALLED_APPS = THIRD_PARTY_APPS + PROJECT_APPS + DJANGO_APPS
if DEBUG:
    INSTALLED_APPS += DEVELOPMENT_APPS
if "channels" in THIRD_PARTY_APPS:
    ASGI_APPLICATION = "mighty_meadow.asgi.application"
else:
    WSGI_APPLICATION = "mighty_meadow.wsgi.application"
ROOT_URLCONF = "mighty_meadow.urls"
# =================================================================================
# CHANNELS / CHAT / WEBSOCKETS
# =================================================================================
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(getenv("REDIS_HOST"), getenv("REDIS_PORT"))],
            # ["unix:///path/to/redis.sock"] # unix domain socket faster than loopback
            #  "symmetric_encryption_keys": [SECRET_KEY],
        },
    },
}
# =================================================================================
# DATABASE / CACHE
# =================================================================================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "TEST": {
            "NAME": BASE_DIR / "db_test.sqlite3",
        },
    }
}
# =================================================================================
# INTERNATIONALIZATION
# =================================================================================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
# =================================================================================
# REST_FRAMEWORK / API
# =================================================================================
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (
        # "rest_framework.permissions.AllowAny",
        # "rest_framework.permissions.IsAdminUser",
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
}

# CORS_ORIGIN_WHITELIST = ('localhost')
CORS_ALLOW_ALL_ORIGINS = True
# ACCOUNT_AUTHENTICATION_METHOD = "username"
# ACCOUNT_EMAIL_VERIFICATION = "none"
CSRF_COOKIE_NAME = "csrftoken"
# =================================================================================
# SECURITY
# =================================================================================
validator = "django.contrib.auth.password_validation"
MIDDLEWARE = (
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)
AUTH_PASSWORD_VALIDATORS = (
    {
        "NAME": f"{validator}.UserAttributeSimilarityValidator",
    },
    {
        "NAME": f"{validator}.MinimumLengthValidator",
    },
    {
        "NAME": f"{validator}.CommonPasswordValidator",
    },
    {
        "NAME": f"{validator}.NumericPasswordValidator",
    },
)
# =================================================================================
# TEMPLATES / STATIC FILES / MEDIA FILES
# =================================================================================
TEMPLATES = (
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
)
SITE_ID = 1
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]  # [BASE_DIR / "build.static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"
CRISPY_TEMPLATE_PACK = "bootstrap4"
LOGIN_REDIRECT_URL = "blog-home"
LOGIN_URL = "login"
CRISPY_TEMPLATE_PACK = "bootstrap4"

from datetime import timedelta

AXES_FAILURE_LIMIT = 3
AXES_ENABLED = False

AXES_COOLOFF_TIME = timedelta(hours=24)
AXES_LOCK_OUT_BY_COMBINATION_USER_AND_IP = True
# AXES_LOCKOUT_TEMPLATE
MIDDLEWARE += ("axes.middleware.AxesMiddleware",)
AUTHENTICATION_BACKENDS = (
    "axes.backends.AxesBackend",
    "django.contrib.auth.backends.ModelBackend",
)
# =================================================================================
# HEROKU / LINODE / DEPLOYMENT SETTINGS
# =================================================================================
import django_heroku

TEST_RUNNER = "django_heroku.HerokuDiscoverRunner"
django_heroku.settings(locals())
