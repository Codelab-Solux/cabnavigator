# Generated by Django 4.1.9 on 2023-06-22 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0012_rename_revenue_ledger_credit_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driverexpense',
            old_name='motive',
            new_name='details',
        ),
        migrations.RenameField(
            model_name='globalexpense',
            old_name='motive',
            new_name='details',
        ),
        migrations.RenameField(
            model_name='vehicleexpense',
            old_name='motive',
            new_name='details',
        ),
    ]