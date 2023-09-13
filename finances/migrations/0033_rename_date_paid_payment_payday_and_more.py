# Generated by Django 4.1 on 2023-08-13 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0032_revenue_month'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='date_paid',
            new_name='payday',
        ),
        migrations.RenameField(
            model_name='payout',
            old_name='date_paid',
            new_name='payday',
        ),
        migrations.RenameField(
            model_name='revenue',
            old_name='date_paid',
            new_name='payday',
        ),
        migrations.RemoveField(
            model_name='driverexpense',
            name='date_posted',
        ),
        migrations.RemoveField(
            model_name='globalexpense',
            name='date_posted',
        ),
        migrations.RemoveField(
            model_name='vehicleexpense',
            name='date_posted',
        ),
    ]
