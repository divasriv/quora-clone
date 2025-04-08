from django.apps import AppConfig

class QuoraAppConfig(AppConfig):
    ''' Configuration for the Quora-like app. '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quora_app'