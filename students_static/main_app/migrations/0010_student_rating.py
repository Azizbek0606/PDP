# Generated by Django 4.2 on 2023-04-08 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
    ]