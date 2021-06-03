# Generated by Django 3.0.5 on 2021-06-03 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20210603_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movie.Movie'),
            preserve_default=False,
        ),
    ]
