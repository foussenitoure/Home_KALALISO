DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'eco',
        'USER': 'myprojectuser',
        'PASSWORD':'password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}