from django.db import models

from core.models import MyModelBase


class Contact(MyModelBase):
    name = models.CharField(max_length=100)
    is_global = models.BooleanField(default=False)

    fone = models.CharField(max_length=14, null=True)
    email = models.EmailField(null=True)

    class Meta:
        db_table = 'contacts'
