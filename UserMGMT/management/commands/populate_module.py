# roles/management/commands/populate_models.py
from django.core.management.base import BaseCommand
from django.apps import apps
from UserMGMT.models import Module, ModelAccess

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for app_config in apps.get_app_configs():
            module, _ = Module.objects.get_or_create(name=app_config.label)
            for model in app_config.get_models():
                ModelAccess.objects.get_or_create(
                    module=module,
                    model_name=model.__name__
                )
        self.stdout.write(self.style.SUCCESS("Modules and Models populated."))
