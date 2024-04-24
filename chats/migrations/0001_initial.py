# Generated by Django 4.1.13 on 2024-04-23 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateThread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=False)),
                ('initiator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='initiator', to=settings.AUTH_USER_MODEL)),
                ('responder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responder', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
