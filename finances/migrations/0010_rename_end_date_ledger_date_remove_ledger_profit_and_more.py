# Generated by Django 4.1.9 on 2023-06-21 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0009_remove_payment_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ledger',
            old_name='end_date',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='ledger',
            name='profit',
        ),
        migrations.RemoveField(
            model_name='ledger',
            name='start_date',
        ),
        migrations.AddField(
            model_name='ledger',
            name='details',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='ledger',
            name='is_audited',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='payment',
            name='is_audited',
            field=models.BooleanField(default='False'),
        ),
    ]