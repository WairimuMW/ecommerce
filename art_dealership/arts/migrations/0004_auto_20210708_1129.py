# Generated by Django 3.1.7 on 2021-07-08 08:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('arts', '0003_auto_20210707_1939'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='CustomerProfile',
        ),
    ]
