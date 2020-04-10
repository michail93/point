from __future__ import absolute_import, unicode_literals

from django.db import transaction

from celery import task

from .models import Abonent


@task()
def hold_task():
    with transaction.atomic():

        for ab in Abonent.objects.select_for_update().filter(status=True, hold__gt=0):
            ab.balance -= ab.hold
            ab.hold = 0
            ab.save()
