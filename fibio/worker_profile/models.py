from tkinter import CASCADE
from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Worker(models.Model):
    user = models.OneToOneField(User, 
        on_delete=models.CASCADE,
        primary_key=True)
    image = models.ImageField(upload_to="profile_images", null=True, blank=True)
    rating = models.FloatField(null=True)
    role = models.ManyToManyField(Category)
    location = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username