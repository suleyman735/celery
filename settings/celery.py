import os
import time
from celery import Celery
from kombu import Queue, Exchange

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')
app = Celery("settings")
app.config_from_object("django.conf:settings", namespace="CELERY")


app.conf.task_queues = [
    Queue('tasks', Exchange('task'),routing_key='tasks',queue_arguments={'x-max-priority':10}),
]

app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1

@app.task(queue = 'tasks')
def t1():
    time.sleep(3)
    return

@app.task(queue = 'tasks')
def t2():
    time.sleep(3)
    return

@app.task(queue = 'tasks')
def t3():
    time.sleep(3)
    return



# app.conf.task_routes = {'newapp.tasks.task1': {'queue':'queue1'},'newapp.tasks.task2': {'queue':'queue2'}}

# app.config.broker_transport_options = {
#     'priority_steps': list(range(10)),
#     'sep':':',
#     'queue_order_strategy':'priority'
# }

app.autodiscover_tasks()

# @app.task
# def add_numbers():
#     print('hello')
#     return
