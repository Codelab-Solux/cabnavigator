# Generated by Django 4.1 on 2023-08-10 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0045_alter_vehicle_serial_number_alter_vehicle_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='color',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
