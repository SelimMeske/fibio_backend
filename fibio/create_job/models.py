from django.db import models
from django.contrib.auth.models import User
from categories.models import Category

# Create your models here.
class JobPost(models.Model):
    PAYMENTS = [
        ('hourly', 'Hourly'),
        ('per_project', 'Per Project')
    ]
    title = models.CharField(max_length=200)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    description = models.CharField(max_length=1000)
    payment = models.CharField(max_length=20, choices=PAYMENTS)
    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.CASCADE
    )
    location = models.CharField(max_length=200)
    time = models.TimeField(auto_now=False, auto_now_add=True)