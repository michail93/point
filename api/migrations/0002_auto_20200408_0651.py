# Generated by Django 2.2.7 on 2020-04-08 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='abonent',
            old_name='uuid',
            new_name='ab_uuid',
        ),
    ]