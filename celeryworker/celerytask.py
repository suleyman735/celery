from celery import Celery


app = Celery('task')
app.config_from_object('celeryconfig',namespace="CELERY")
app.conf.imports = ('newapp.tasks')
app.autodiscover_tasks()

