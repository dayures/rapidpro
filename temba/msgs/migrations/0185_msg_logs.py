# Generated by Django 4.0.7 on 2022-08-25 19:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("msgs", "0184_alter_msg_failed_reason"),
    ]

    operations = [
        migrations.AddField(
            model_name="msg",
            name="logs",
            field=django.contrib.postgres.fields.ArrayField(base_field=models.UUIDField(), null=True, size=None),
        ),
    ]