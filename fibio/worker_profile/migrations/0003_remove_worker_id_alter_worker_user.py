# Generated by Django 4.0.1 on 2022-01-16 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('worker_profile', '0002_remove_worker_role_alter_worker_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='id',
        ),
        migrations.AlterField(
            model_name='worker',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]