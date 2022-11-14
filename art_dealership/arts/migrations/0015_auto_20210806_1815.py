# Generated by Django 3.1.7 on 2021-08-06 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0014_auto_20210731_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('Booked', 'Booked'), ('Sold', 'Sold')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='custprof',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='delivery',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]