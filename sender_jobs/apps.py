from django.apps import AppConfig


class SenderJobsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sender_jobs'
class CarrierJobsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carrier_jobs'
