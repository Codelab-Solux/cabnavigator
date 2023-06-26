# Generated by Django 4.1.9 on 2023-06-02 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0005_remove_driver_is_married_driver_martital_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateTimeField(blank=True)),
                ('expiry_date', models.DateTimeField(blank=True)),
                ('issuing_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('is_valid', models.BooleanField(default='False')),
                ('posted_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='driver_docs')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.documenttype')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(default='', max_length=255)),
                ('make', models.CharField(default='', max_length=255)),
                ('model', models.CharField(default='', max_length=255)),
                ('plate_number', models.CharField(default='', max_length=255)),
                ('year', models.IntegerField(default='')),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('transmission', models.CharField(choices=[('Manuelle', 'Manuelle'), ('Automatique', 'Automatique')], default='', max_length=50)),
                ('state', models.CharField(choices=[('Neuf', 'Neuf'), ('Usagé\xa0', 'Usagé\xa0')], default='', max_length=50)),
                ('color', models.CharField(default='', max_length=255)),
                ('supplier', models.CharField(default='', max_length=255)),
                ('management', models.CharField(choices=[('Neuf', 'Neuf'), ('Usagé\xa0', 'Usagé\xa0')], default='', max_length=50)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='vehicles')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateTimeField(blank=True)),
                ('expiry_date', models.DateTimeField(blank=True)),
                ('issuing_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('is_valid', models.BooleanField(default='False')),
                ('posted_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='vehicle_docs')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.documenttype')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.vehicle', unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
