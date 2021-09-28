from django.apps import AppConfig


class LearnConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'learn'

    def ready(self):
        from learn.infrastructure.infrastructure_module import InfrastructureModule
        infrastructure_module = InfrastructureModule()
        infrastructure_module.load()