# Generated by Django 4.2.4 on 2023-08-15 22:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sauces', '0004_remove_artist_direct_uploader_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sauce',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sauce',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='hash',
            name='method',
            field=models.IntegerField(choices=[(0, 'Perceptual'), (1, 'Average'), (2, 'Differential'), (3, 'Wavelet')], default=0),
        ),
    ]
