# Generated by Django 3.1.7 on 2021-07-06 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='atype',
            new_name='art_type',
        ),
    ]
