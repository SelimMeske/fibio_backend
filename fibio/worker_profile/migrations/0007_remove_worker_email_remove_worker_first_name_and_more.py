# Generated by Django 4.0.1 on 2022-01-17 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worker_profile', '0006_worker_first_name_worker_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='email',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='last_name',
        ),
    ]
