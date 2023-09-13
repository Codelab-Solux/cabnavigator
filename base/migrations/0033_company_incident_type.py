# Generated by Django 4.1.9 on 2023-07-17 09:52

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0032_incidenttype_incident_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('reg_number', models.CharField(default='', max_length=255)),
                ('fiscal_id', models.CharField(default='', max_length=255)),
                ('legal_status', models.CharField(choices=[('EURL', 'EURL'), ('SARL', 'SARL'), ('SARLU', 'SARLU'), ('SAS', 'SAS'), ('SA', 'SA')], default='', max_length=50)),
                ('social_capital', models.CharField(default='', max_length=255)),
                ('address', models.CharField(default='', max_length=255)),
                ('city', models.CharField(default='', max_length=255)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('phone', models.CharField(default='', max_length=255)),
                ('email', models.EmailField(default='', max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='companies/')),
            ],
        ),
        migrations.AddField(
            model_name='incident',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.incidenttype'),
        ),
    ]
