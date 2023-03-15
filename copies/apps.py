from django.apps import AppConfig


class CopiesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "copies"
    
    def ready(self):
        print("Starting Scheduler ...")
        from .loan_schedules import loan_updater
        loan_updater.start()
