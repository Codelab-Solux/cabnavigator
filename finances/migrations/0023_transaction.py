# Generated by Django 4.1.9 on 2023-07-05 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0022_payout_driver'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('debit', 'Encaissement'), ('credit', 'Décaissement')], max_length=50)),
                ('amount', models.IntegerField(blank=True, default='0')),
                ('details', models.CharField(blank=True, max_length=1000, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('is_audited', models.BooleanField(default=False)),
            ],
        ),
    ]