from django.apps import AppConfig


class StudyAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'study_auth'

    def ready(self):
        from . import signals
