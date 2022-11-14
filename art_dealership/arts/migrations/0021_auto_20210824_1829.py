# Generated by Django 3.1.7 on 2021-08-24 15:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0020_auto_20210822_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
    ]
