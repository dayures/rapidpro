# Generated by Django 2.2.20 on 2021-07-28 14:27

from django.db import migrations, models

BATCH_SIZE = 5000


def zeroize_ticket_count(apps, schema_editor):  # pragma: no cover
    Contact = apps.get_model("contacts", "Contact")
    num_updated = 0
    max_id = -1
    while True:
        batch_ids = list(
            Contact.objects
            .filter(id__gt=max_id, ticket_count=None)
            .values_list("id", flat=True)
            .order_by("id")[:BATCH_SIZE]
        )
        if not batch_ids:
            break

        Contact.objects.filter(id__in=batch_ids).update(ticket_count=0)
        max_id = batch_ids[-1]
        num_updated += len(batch_ids)

        print(f"Updated {num_updated} contacts")


def reverse(apps, schema_editor):  # pragma: no cover
    pass


def apply_manual():  # pragma: no cover
    from django.apps import apps

    zeroize_ticket_count(apps, None)


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0139_contact_ticket_count"),
    ]

    operations = [
        migrations.RunPython(zeroize_ticket_count, reverse),
        migrations.AlterField(
            model_name="contact",
            name="ticket_count",
            field=models.IntegerField(default=0),
        ),
    ]