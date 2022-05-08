"""
Model helper
"""
###
# Libraries
###
from django.db import models
from django.utils import timezone


###
# Helpers
###
class TimestampModel(models.Model):
    """Extend this model if you wish."""

    class Meta:
        abstract = True

    created_at = models.DateTimeField(null=False, blank=True, default=timezone.localtime)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)

    def save(self, *args, **kwargs):
        if kwargs.get('update_fields'):
            kwargs['update_fields'] = list(set(list(kwargs['update_fields']) + ['updated_at']))
        return super().save(*args, **kwargs)