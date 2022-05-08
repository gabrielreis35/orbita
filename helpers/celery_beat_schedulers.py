from django_celery_beat.models import PeriodicTask
from django_celery_beat.schedulers import DatabaseScheduler, ModelEntry


class CustomModelEntry(ModelEntry):

    @classmethod
    def from_entry(cls, name, app=None, **entry):
        """Override method to not update tasks on Celery restart"""
        obj, _ = PeriodicTask._default_manager.get_or_create(
            name=name, defaults=cls._unpack_fields(**entry),
        )
        return cls(obj, app=app)


class CustomDatabaseScheduler(DatabaseScheduler):
    """Override DatabaseScheduler Entry to not update tasks on Celery restart"""
    Entry = CustomModelEntry
