from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models, transaction
from django.forms import model_to_dict
from django_changed_fields import ChangedFieldsMixin


class Log(models.Model):
    user = models.PositiveIntegerField(null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    fields = models.TextField()
    old_value_fields = models.TextField()
    new_value_fields = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'log'


class ModelSafelyDeleteQuerySet(models.QuerySet):
    @transaction.atomic
    def delete(self):
        now = datetime.now()
        Log.objects.bulk_create(
            map(lambda item: Log(
                user=getattr(item, 'owner_id', None),
                content_object=item,
                fields='deleted_at',
                new_value_fields=now,
                old_value_fields='None',
            ), self)
        )
        self.update(deleted_at=now)


class ModelSafelyDeleteManager(models.Manager):
    def get_queryset(self):
        return ModelSafelyDeleteQuerySet(self.model, using=self._db).filter(deleted_at__isnull=True)


class MyModelBase(ChangedFieldsMixin, models.Model):
    objects = ModelSafelyDeleteManager()
    default_objects = ModelSafelyDeleteQuerySet.as_manager()

    owner = models.ForeignKey(get_user_model(), models.CASCADE)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True

    @transaction.atomic
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        changed_fields = self.change_fields()
        if len(changed_fields):
            new_value_fields = model_to_dict(self, fields=changed_fields)
            new_value_fields = ', '.join(map(lambda new: str(new_value_fields.get(new)), changed_fields))

            last_queryset = self.last_queryset()
            old_value_fields = ''
            if last_queryset:
                old_value_fields = model_to_dict(last_queryset, fields=changed_fields)
                old_value_fields = ', '.join(map(lambda old: str(old_value_fields.get(old)), changed_fields))

            super().save(force_insert, force_update, using, update_fields)

            Log(
                user=getattr(self, 'owner_id', None),
                content_object=self,
                fields=', '.join(changed_fields),
                new_value_fields=new_value_fields,
                old_value_fields=old_value_fields,
            ).save(force_insert, force_update, using, update_fields)

            return
        super().save(force_insert, force_update, using, update_fields)

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = datetime.now()
        self.save(using=using)
