# Generated by Django 4.0.9 on 2023-02-23 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("channels", "0158_squashed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="channel",
            name="claim_code",
            field=models.CharField(blank=True, max_length=16, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="channel",
            name="device",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="channel",
            name="last_seen",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="channel",
            name="os",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="channel",
            name="secret",
            field=models.CharField(blank=True, max_length=64, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="channel",
            name="tps",
            field=models.IntegerField(null=True),
        ),
    ]
