# Generated by Django 2.2.7 on 2020-04-08 06:46

import api.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abonent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('full_name', models.CharField(max_length=150, validators=[api.models.validate_full_name])),
                ('balance', models.DecimalField(decimal_places=2, max_digits=12)),
                ('hold', models.DecimalField(decimal_places=2, max_digits=6)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
