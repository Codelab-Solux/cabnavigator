# Generated by Django 4.1.9 on 2023-06-15 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_remove_vehicle_id_alter_vehicle_plate_number_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Incident',
        ),
    ]
