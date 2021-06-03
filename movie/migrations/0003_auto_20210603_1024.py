# Generated by Django 3.0.5 on 2021-06-03 04:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_movie_platform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('description', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='movie',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movie.StreamPlatforms'),
        ),
    ]
