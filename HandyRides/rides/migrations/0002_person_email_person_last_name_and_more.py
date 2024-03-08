# Generated by Django 5.0.2 on 2024-02-22 01:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rides", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="email",
            field=models.CharField(default=str, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="person",
            name="last_name",
            field=models.CharField(default=str, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="person",
            name="origination_state",
            field=models.CharField(default=str, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="person",
            name="vehicle_type",
            field=models.CharField(default=str, max_length=64),
            preserve_default=False,
        ),
    ]
