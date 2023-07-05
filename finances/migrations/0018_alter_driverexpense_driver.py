# Generated by Django 4.1.9 on 2023-07-03 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finances', '0017_delete_contract_alter_vehicleexpense_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverexpense',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]