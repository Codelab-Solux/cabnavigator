# Generated by Django 4.1.9 on 2023-07-03 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_alter_driver_user_alter_partnerdocument_expiry_date_and_more'),
        ('finances', '0018_alter_driverexpense_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverexpense',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.driver'),
        ),
    ]