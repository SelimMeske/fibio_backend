from django import forms
from .models import JobPost

class CreateJob(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['title', 'description', 'payment', 'category', 'location']
