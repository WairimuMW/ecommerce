# Generated by Django 3.1.7 on 2021-08-24 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0021_auto_20210824_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='art',
            name='date_added',
        ),
    ]