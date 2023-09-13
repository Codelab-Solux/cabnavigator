# Generated by Django 4.1 on 2023-08-10 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0044_remove_vehicle_management_alter_driver_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='serial_number',
            field=models.CharField(blank=True, default='', max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='supplier',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
