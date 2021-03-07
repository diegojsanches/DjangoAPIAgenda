import uuid

from django.db import models

from core.models import MyModelBase


def pathUploadContactImage(instance, filename):
    return f'users/photos/{uuid.uuid4()}_{filename}'


class Contact(MyModelBase):
    name = models.CharField(max_length=100)
    is_public = models.BooleanField(default=False)
    image = models.ImageField(upload_to=pathUploadContactImage, blank=True)

    fone = models.CharField(max_length=14, null=True)
    email = models.EmailField(null=True)

    class Meta:
        db_table = 'contacts'
