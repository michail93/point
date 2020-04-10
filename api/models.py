import uuid
import re
from decimal import Decimal

from django.db import models
from django.core.exceptions import ValidationError
from django.db import transaction


def validate_full_name(value):
    regex = re.compile('[=,.+\[\]@_!#$%^&*()<>?/\|}{~:]')
    regex2 = re.compile('[0-9]')

    if type(value) is not str:
        raise ValidationError("value must be a string")

    if regex.search(value) or regex2.search(value):
        raise ValidationError("value contains forbidden symbols")

    eng = bool(re.findall(r'[A-za-z]', value))
    rus = bool(re.findall(r'[А-яа-я]', value))

    if not eng != rus:
        raise ValidationError("value must contain only latin or cyrillic symbols")


class Abonent(models.Model):
    ab_uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    full_name = models.CharField(max_length=150, null=False, blank=False)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    hold = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.BooleanField(default=False)

    @classmethod
    def refill_balance(cls, ab_uuid, amount):
        with transaction.atomic():
            to_abontent = cls.objects.select_for_update().get(ab_uuid=ab_uuid)
            to_abontent.balance += Decimal(amount)
            to_abontent.save()

        return to_abontent.balance

    @classmethod
    def decreacse_balance(cls, ab_uuid, amount):
        with transaction.atomic():
            to_abontent = cls.objects.select_for_update().get(ab_uuid=ab_uuid)
            to_abontent.balance -= Decimal(amount)
            to_abontent.save()

        return to_abontent.balance

    def save(self, *args, **kwargs):
        validate_full_name(self.full_name)
        return super(Abonent, self).save(*args, **kwargs)
