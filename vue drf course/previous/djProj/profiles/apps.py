from django.apps import AppConfig

# from . import signals


class ProfilesConfig(AppConfig):
    name = 'profiles'

    def ready(self):
        from . import signals
