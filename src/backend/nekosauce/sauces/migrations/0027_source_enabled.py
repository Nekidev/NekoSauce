# Generated by Django 4.2.5 on 2023-09-28 03:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sauces", "0026_hash_hash_bits_idx"),
    ]

    operations = [
        migrations.AddField(
            model_name="source",
            name="enabled",
            field=models.BooleanField(default=True),
        ),
    ]
