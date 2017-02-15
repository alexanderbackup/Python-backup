from django import forms
from .models import User


class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'


class Login(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    password = forms.CharField(widget=forms.PasswordInput)
