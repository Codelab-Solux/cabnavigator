# Generated by Django 4.1.9 on 2023-07-03 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_alter_driver_user_alter_partnerdocument_expiry_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='driver',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
    ]