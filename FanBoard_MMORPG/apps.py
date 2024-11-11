from django.apps import AppConfig


class FanboardMmorpgConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FanBoard_MMORPG'


    def ready(self):
        from . import signals  # выполнение модуля -> регистрация сигналов