# Generated by Django 4.2.4 on 2023-08-20 07:38

from django.db import migrations
import nekosauce.sauces.utils.fields


class Migration(migrations.Migration):
    dependencies = [
        ("sauces", "0012_delete_artist"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="hash16bits",
            options={
                "verbose_name": "Hash (16^2 Bits)",
                "verbose_name_plural": "Hashes (16^2 Bits)",
            },
        ),
        migrations.AlterModelOptions(
            name="hash32bits",
            options={
                "verbose_name": "Hash (32^2 Bits)",
                "verbose_name_plural": "Hashes (32^2 Bits)",
            },
        ),
        migrations.AlterModelOptions(
            name="hash64bits",
            options={
                "verbose_name": "Hash (64^2 Bits)",
                "verbose_name_plural": "Hashes (64^2 Bits)",
            },
        ),
        migrations.AlterModelOptions(
            name="hash8bits",
            options={
                "verbose_name": "Hash (8^2 Bits)",
                "verbose_name_plural": "Hashes (8^2 Bits)",
            },
        ),
        migrations.AlterField(
            model_name="hash16bits",
            name="bits",
            field=nekosauce.sauces.utils.fields.BitField(db_index=True, max_length=256),
        ),
        migrations.AlterField(
            model_name="hash32bits",
            name="bits",
            field=nekosauce.sauces.utils.fields.BitField(
                db_index=True, max_length=1024
            ),
        ),
        migrations.AlterField(
            model_name="hash64bits",
            name="bits",
            field=nekosauce.sauces.utils.fields.BitField(
                db_index=True, max_length=4096
            ),
        ),
        migrations.AlterField(
            model_name="hash8bits",
            name="bits",
            field=nekosauce.sauces.utils.fields.BitField(db_index=True, max_length=64),
        ),
    ]
