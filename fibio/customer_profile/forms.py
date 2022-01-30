from django import forms

class ClientRegistration(forms.Form):
    username = forms.CharField(max_length=255)
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label="Confirm password",
        help_text="Repeate the password."
    )
    email = forms.EmailField()
    

