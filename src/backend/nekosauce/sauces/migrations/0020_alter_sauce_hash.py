# Generated by Django 4.2.4 on 2023-09-06 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("sauces", "0019_hash_alter_hash32bits_unique_together_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sauce",
            name="hash",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="sauces",
                to="sauces.hash",
            ),
        ),
    ]
