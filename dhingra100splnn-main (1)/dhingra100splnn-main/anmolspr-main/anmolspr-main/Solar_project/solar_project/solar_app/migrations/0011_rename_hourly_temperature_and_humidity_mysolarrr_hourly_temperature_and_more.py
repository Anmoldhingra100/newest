# Generated by Django 5.0.7 on 2024-07-30 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar_app', '0010_alter_mysolarrr_hourly_temperature_and_humidity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mysolarrr',
            old_name='Hourly_temperature_and_humidity',
            new_name='Hourly_temperature',
        ),
        migrations.RenameField(
            model_name='mysolarrr',
            old_name='Investor_power_distribution',
            new_name='Invertor_power_distribution',
        ),
        migrations.AddField(
            model_name='mysolarrr',
            name='humidity',
            field=models.IntegerField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='mysolarrr',
            name='Performance',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
