from django.db import models
from location_field.models.plain import PlainLocationField
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    email = models.EmailField(max_length=500)

    def __str__(self):
        return self.user.username