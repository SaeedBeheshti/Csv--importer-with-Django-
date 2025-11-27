from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'csv_importer.settings')

app = Celery('csv_importer')


app.config_from_object('django.conf:settings', namespace='CELERY')

# broker Redis
app.conf.broker_url = 'redis://redis:6379/0'
app.conf.result_backend = 'redis://redis:6379/0'

app.autodiscover_tasks()
