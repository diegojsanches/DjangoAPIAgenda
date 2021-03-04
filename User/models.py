import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import gettext_lazy as _


def pathUploadProfilePhoto(instance, filename):
    return f'users/photos/{uuid.uuid4()}_{filename}'


class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Username and password are required. Other fields are optional.
    """

    first_name = None
    last_name = None

    email = models.EmailField(_('email address'), unique=True, blank=True)
    name = models.CharField(_('name'), max_length=150, blank=True)

    photo = models.ImageField(upload_to=pathUploadProfilePhoto, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta(AbstractUser.Meta):
        db_table = 'users'
        swappable = 'AUTH_USER_MODEL'
