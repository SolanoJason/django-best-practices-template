from .base import *

DEBUG = True

INTERNAL_IPS = [
    "127.0.0.1",
]

ALLOWED_HOSTS = [".localhost", "127.0.0.1", "[::1]"]  # Default when debug is True

SECRET_KEY = {{ secret_key }}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
