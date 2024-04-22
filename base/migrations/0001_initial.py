# Generated by Django 4.1.9 on 2024-04-22 03:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
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
                ('logo', models.ImageField(blank=True, null=True, upload_to='company/logos')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='company/banners')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('description', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('civility', models.CharField(choices=[('M.', 'M.'), ('Mme.', 'Mme'), ('Mlle.', 'Mlle')], default='', max_length=50)),
                ('martital_status', models.CharField(choices=[('Célibataire', 'Célibataire'), ('Marié(e)', 'Marié(e)'), ('Divorcé(e)', 'Divorcé(e)'), ('Voeuf(ve)', 'Voeuf(ve)')], default='', max_length=50)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('nationality', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('place_of_birth', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('city', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('phone', models.CharField(default='', max_length=255)),
                ('address', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('bio', models.CharField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='drivers')),
                ('date_joined', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('score', models.IntegerField(blank=True, default='100')),
                ('observation', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IncidentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('description', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commission', models.IntegerField(blank=True, default='0')),
                ('civility', models.CharField(choices=[('M.', 'M.'), ('Mme.', 'Mme'), ('Mlle.', 'Mlle')], default='', max_length=50)),
                ('first_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('martital_status', models.CharField(choices=[('Célibataire', 'Célibataire'), ('Marié(e)', 'Marié(e)'), ('Divorcé(e)', 'Divorcé(e)'), ('Voeuf(ve)', 'Voeuf(ve)')], default='', max_length=50)),
                ('nationality', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('place_of_birth', models.CharField(default='', max_length=255)),
                ('city', models.CharField(default='', max_length=255)),
                ('phone', models.CharField(default='', max_length=255)),
                ('address', models.CharField(default='', max_length=255)),
                ('bio', models.CharField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='partners/')),
                ('date_joined', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('supplier', models.CharField(blank=True, max_length=255, null=True)),
                ('make', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('plate_number', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('serial_number', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('state', models.CharField(choices=[('Neuf', 'Neuf'), ('Usagé\xa0', 'Usagé\xa0')], max_length=50)),
                ('transmission', models.CharField(choices=[('Manuelle', 'Manuelle'), ('Automatique', 'Automatique')], max_length=50)),
                ('color', models.CharField(blank=True, max_length=255, null=True)),
                ('cost', models.IntegerField(default='0')),
                ('commission', models.IntegerField(default='10')),
                ('image', models.ImageField(blank=True, null=True, upload_to='vehicles/')),
                ('is_active', models.BooleanField(default=True)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('first_driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='first_driver', to='base.driver')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('second_driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='second_driver', to='base.driver')),
                ('third_driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='third_driver', to='base.driver')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateTimeField(blank=True)),
                ('expiry_date', models.DateTimeField(blank=True, null=True)),
                ('issuing_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('is_valid', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='vehicle_docs/')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.documenttype')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True)),
                ('article', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='tips/images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='tips/videos/')),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PartnerDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateTimeField(blank=True, null=True)),
                ('expiry_date', models.DateTimeField(blank=True, null=True)),
                ('issuing_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('is_valid', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='partner_docs/')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.partner')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.documenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('object_id', models.PositiveIntegerField()),
                ('is_read', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repairability', models.CharField(blank=True, choices=[('repairable', 'Reparable'), ('unrepairable', 'Irreparable')], default='', max_length=50, null=True)),
                ('mobility', models.CharField(blank=True, choices=[('mobile', 'Mobilisé'), ('immobile', 'Immobilisé')], default='', max_length=50, null=True)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('place', models.CharField(max_length=128)),
                ('cost', models.IntegerField(blank=True, default=0, null=True)),
                ('is_solved', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='incidents/')),
                ('comment', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.driver')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.incidenttype')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='DriverDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateTimeField(blank=True)),
                ('expiry_date', models.DateTimeField(blank=True)),
                ('issuing_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('is_valid', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='driver_docs/')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.driver')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.documenttype')),
            ],
        ),
        migrations.AddField(
            model_name='driver',
            name='vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.vehicle'),
        ),
        migrations.CreateModel(
            name='ChatNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
