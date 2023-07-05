# Generated by Django 4.2 on 2023-06-01 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0003_tutor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateTimeField(blank=True)),
                ('expiry_date', models.DateTimeField(blank=True)),
                ('issue_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('is_valid', models.BooleanField(default='False')),
                ('posted_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='drivers')),
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
                ('nationality', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('place_of_birth', models.CharField(default='', max_length=255)),
                ('city', models.CharField(default='', max_length=255)),
                ('phone', models.CharField(default='', max_length=255)),
                ('address', models.CharField(default='', max_length=255)),
                ('bio', models.CharField(blank=True, max_length=1000, null=True)),
                ('is_married', models.BooleanField(default='False')),
                ('image', models.ImageField(blank=True, null=True, upload_to='drivers')),
                ('date_joined', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('severity', models.CharField(blank=True, choices=[('mineur', 'Mineur'), ('majeur', 'Majeur'), ('fatal', 'Fatal')], default='', max_length=50, null=True)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('posted_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='incidents')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='author',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='user',
        ),
        migrations.DeleteModel(
            name='Advert',
        ),
        migrations.DeleteModel(
            name='Blogpost',
        ),
        migrations.DeleteModel(
            name='Tutor',
        ),
        migrations.AddField(
            model_name='document',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.documenttype'),
        ),
        migrations.AddField(
            model_name='document',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]