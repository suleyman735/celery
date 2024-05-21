import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')
app = Celery("celery")
app.config_from_object("django.conf:settings", namespace="CELERY")


@app.task
def add_numbers():
    print('hello')
    return

app.autodiscover_tasks()