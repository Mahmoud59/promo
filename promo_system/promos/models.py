from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _

from users.models import UserProfile


class Promo(TimeStampedModel):
    class PromoStatus(models.TextChoices):
        ACTIVE = 'active', _('active')
        ON_HOLD = 'on_hold', _('on_hold')

    type = models.TextField('Promo Type')
    code = models.CharField('Promo Code', max_length=10, unique=True)
    start_time = models.DateTimeField('Promo Start Time')
    end_time = models.DateTimeField('Promo End Time')
    amount = models.FloatField('Promo Amount')
    description = models.TextField('Promo Description')
    status = models.TextField(choices=PromoStatus.choices,
                              default=PromoStatus.ACTIVE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
