# Generated by Django 4.2 on 2023-04-07 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_student_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='img',
            field=models.ImageField(blank=True, upload_to='photos/'),
        ),
    ]
