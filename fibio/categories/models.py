from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField()

    def __str__(self):
        return self.name
