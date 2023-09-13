# Generated by Django 4.1.9 on 2023-07-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0026_bank_acc_number_revenue_partner_delete_dividend'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(blank=True, max_length=1000, null=True)),
                ('debit', models.IntegerField(blank=True, default='0')),
                ('credit', models.IntegerField(blank=True, default='0')),
                ('date', models.DateField(blank=True, null=True)),
                ('is_audited', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MobileVault',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator', models.CharField(default='', max_length=255)),
                ('phone_number', models.CharField(default='', max_length=255, unique=True)),
                ('debit', models.IntegerField(blank=True, default='0')),
                ('credit', models.IntegerField(blank=True, default='0')),
                ('balance', models.IntegerField(blank=True, default='0')),
            ],
        ),
        migrations.RenameModel(
            old_name='Bank',
            new_name='BankVault',
        ),
        migrations.RenameModel(
            old_name='Cashdesk',
            new_name='CashVault',
        ),
    ]