# Generated by Django 3.2.4 on 2021-06-07 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_review_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='number_rating',
            field=models.IntegerField(default=0),
        ),
    ]
