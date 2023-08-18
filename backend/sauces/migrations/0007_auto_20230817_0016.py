# Generated by Django 4.2.4 on 2023-08-17 03:16

from django.db import migrations


def create_pg_similarity(apps, schema_editor):
    schema_editor.execute("CREATE EXTENSION pg_similarity;")


def drop_pg_similarity(apps, schema_editor):
    schema_editor.execute("DROP EXTENSION IF EXISTS pg_similarity;")


class Migration(migrations.Migration):

    dependencies = [
        ('sauces', '0006_alter_sauce_height_alter_sauce_width_and_more'),
    ]

    operations = [
        migrations.RunPython(create_pg_similarity, reverse_code=drop_pg_similarity, atomic=True)
    ]
