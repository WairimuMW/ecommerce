# Generated by Django 3.1.7 on 2021-08-24 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0025_art_date_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='date_added',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
