from django import forms
from .models import Profile
from django.contrib.auth import authenticate,login,logout,get_user_model

user=get_user_model()

class SignUpForm(forms.ModelForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = Profile
        fields = ('username', 'password', 'email' ,'birth_date' )

class LogInForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username','password')