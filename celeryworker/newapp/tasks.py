from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def task1():
    return

@shared_task
def task2():
    return