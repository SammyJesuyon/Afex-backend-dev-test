from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devtest.settings')

app = Celery('devtest')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'scheduled_task': {
        'task': 'crm.tasks.populate_clients',
        'schedule': 3600.0,
        'args': ('true',),
    },
}