from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        help_text='',  
        label="Username"
    )
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")

        if password and confirm and password != confirm:
            raise ValidationError("Passwords do not match")
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


