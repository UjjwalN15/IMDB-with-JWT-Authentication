# Generated by Django 5.0.7 on 2024-08-04 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='added_on',
            field=models.DateTimeField(default='2024-08-04T11:31:50.468382+05:45'),
        ),
    ]
