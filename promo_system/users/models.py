import uuid

from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel


class UserAccount(TimeStampedModel):
    class Meta:
        abstract = True

    uuid = models.UUIDField('User ID', primary_key=True, default=uuid.uuid4)
    username = models.TextField('Username', unique=True)
    address = models.TextField('Address', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Admin(UserAccount):
    pass


class UserProfile(UserAccount):
    mobile_number = models.CharField('Mobile Number', max_length=11)
