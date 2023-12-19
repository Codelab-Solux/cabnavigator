# Generated by Django 4.1.9 on 2023-12-19 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        ('finances', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='vehicle',
            field=models.ForeignKey(default='007tog', on_delete=django.db.models.deletion.CASCADE, to='base.vehicle'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='revenue',
            name='vehicle',
            field=models.ForeignKey(default='007tog', on_delete=django.db.models.deletion.CASCADE, to='base.vehicle'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicleexpense',
            name='vehicle',
            field=models.ForeignKey(default='007tog', on_delete=django.db.models.deletion.CASCADE, to='base.vehicle'),
            preserve_default=False,
        ),
    ]
