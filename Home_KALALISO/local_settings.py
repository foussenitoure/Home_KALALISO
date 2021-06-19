DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'kala',
        'USER': 'myprojectuser',
        'PASSWORD':'kaladb',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}