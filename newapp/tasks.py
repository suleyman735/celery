from __future__ import absolute_import, unicode_literals
import time
from celery import shared_task

# @shared_task
# def sharedtask():
#     print('shared task from new app')
#     return

# @shared_task
# def task1():
#     return

# @shared_task
# def task2():
#     return

@shared_task
def tp1(queue='celery'):
    time.sleep(3)
    return

@shared_task
def tp2(queue='celery:1'):
    time.sleep(3)
    return
@shared_task
def tp3(queue='celery:2'):
    time.sleep(3)
    return
@shared_task
def tp4(queue='celery:3'):
    time.sleep(3)
    return