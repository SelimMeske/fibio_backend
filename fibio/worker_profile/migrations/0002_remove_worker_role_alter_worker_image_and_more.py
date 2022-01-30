# Generated by Django 4.0.1 on 2022-01-16 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker_profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='role',
        ),
        migrations.AlterField(
            model_name='worker',
            name='image',
            field=models.ImageField(null=True, upload_to='profile_images'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='rating',
            field=models.FloatField(null=True),
        ),
    ]
