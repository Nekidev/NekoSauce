# Generated by Django 4.2.4 on 2023-09-06 06:57

from django.db import migrations
import nekosauce.sauces.utils.fields


class Migration(migrations.Migration):
    dependencies = [
        ("sauces", "0020_alter_sauce_hash"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hash",
            name="bits",
            field=nekosauce.sauces.utils.fields.BitField(
                editable=False,
                max_length=256,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
