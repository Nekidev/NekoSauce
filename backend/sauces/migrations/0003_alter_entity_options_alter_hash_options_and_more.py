# Generated by Django 4.2.4 on 2023-08-15 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sauces', '0002_entity_tags_sauce_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entity',
            options={'verbose_name': 'Entity', 'verbose_name_plural': 'Entities'},
        ),
        migrations.AlterModelOptions(
            name='hash',
            options={'verbose_name': 'Hash', 'verbose_name_plural': 'Hashes'},
        ),
        migrations.AlterField(
            model_name='artsauce',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='art_sauces', to='sauces.artist'),
        ),
    ]