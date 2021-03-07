from django.db import models

from Contact.models import Contact
from core.models import MyModelBase


class Address(MyModelBase):
    contact = models.ForeignKey(Contact, models.CASCADE, 'addresses')

    zip_code = models.CharField(max_length=9, blank=True, null=True)
    street = models.CharField(max_length=80)
    number = models.CharField(max_length=6, blank=True, null=True)
    complement = models.CharField(max_length=60, blank=True, null=True)
    district = models.CharField(max_length=40, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        db_table = 'addresses'
