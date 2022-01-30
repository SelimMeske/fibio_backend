from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        return username
    def clean_password(self):
        password = self.cleaned_data['password']
        return password