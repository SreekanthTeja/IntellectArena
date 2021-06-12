from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Username',)
    email=forms.EmailField(max_length=64, help_text='Enter a valid email address')
    password1=forms.CharField(label='Password', help_text='password must be min 8 letters and must match', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2=forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username= forms.CharField(label='Email',max_length=124)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    


