from django.contrib.auth import get_user_model
from django import forms
from django.forms import ValidationError
from .models import Worker
from categories.models import Category

User = get_user_model()

# Get all categories from the database
roles_DB = Category.objects.all()

ROLES = []

for role in roles_DB:
    role_tup = (role.id, role.name)
    ROLES.append(role_tup)

class WorkerProfile(forms.Form):
        username = forms.CharField(max_length=100, help_text="Must be unique.")
        first_name = forms.CharField(max_length=100)
        last_name = forms.CharField(max_length=100)
        password = forms.CharField(widget=forms.PasswordInput())
        password2 = forms.CharField(
            label="Confirm password", 
            widget=forms.PasswordInput(), 
            help_text="Repeate the password.")
        email = forms.EmailField()
        profile_picture = forms.ImageField()
        role = forms.MultipleChoiceField(choices=ROLES)
        location = forms.CharField(max_length=100)
        phone_number = forms.CharField(max_length=100)

        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get('password')
            password2 = cleaned_data.get('password2')
            email = cleaned_data.get('email')

            if password != password2:
                raise ValidationError(
                    'Passwords are not matching.'
                )
            elif User.objects.filter(email=email):
                raise ValidationError(
                    'User with the same email already exists.'
                )
        

