# Generated by Django 4.1.9 on 2023-06-21 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0006_payment_rename_driverpayout_payout_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investmentrecap',
            name='driver_count',
        ),
    ]