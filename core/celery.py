"""
Orbita Celery Configuration
"""
###
# Libraries
###
import os

from celery import Celery
from django.conf import settings

###
# Main Configuration
###
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")
app.config_from_object("django.conf:settings")
app.conf.beat_scheduler = "django_celery_beat.schedulers.DatabaseScheduler"

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(
    name='test',
    bind=True
)
def test_cron(self):
    print('aqui')