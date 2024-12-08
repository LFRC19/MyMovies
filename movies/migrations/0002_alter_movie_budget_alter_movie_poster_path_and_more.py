# Generated by Django 5.1.2 on 2024-11-17 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='budget',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster_path',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='revenue',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tmdb_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]