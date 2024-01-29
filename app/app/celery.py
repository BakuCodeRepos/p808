from __future__ import absolute_import, unicode_literals

import logging
import os

from django.conf import settings
from celery import Celery

logger = logging.getLogger("Celery")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

app = Celery("app")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print("Request: {self.request}")

if settings.DEBUG:
    app.conf.update(
        BROKER_URL='redis://localhost:6379/0',
        CELERYBEAT_SCHEDULER='django_celery_beat.schedulers:DatabaseScheduler',
        CELERY_RESULT_BACKEND='redis://localhost:6379/1',
        CELERY_DISABLE_RATE_LIMITS=True,
        CELERY_ACCEPT_CONTENT=['json', ],
        CELERY_TASK_SERIALIZER='json',
        CELERY_RESULT_SERIALIZER='json',
        # CELERY_TIMEZONE='Asia/Baku',
    )
else:
    app.conf.update(
        BROKER_URL='redis://:20zSjJz09azhxCrA@redis:6379/0',
        CELERYBEAT_SCHEDULER='django_celery_beat.schedulers:DatabaseScheduler',
        CELERY_RESULT_BACKEND='redis://:20zSjJz09azhxCrA@redis:6379/1',
        CELERY_DISABLE_RATE_LIMITS=True,
        CELERY_ACCEPT_CONTENT=['json', ],
        CELERY_TASK_SERIALIZER='json',
        CELERY_RESULT_SERIALIZER='json',
        # CELERY_TIMEZONE='Asia/Baku',
    )
