from django import forms
from django.contrib.auth.models import User
from first_app1.models import Userprofile

class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        

class Userprofileform(forms.ModelForm):
    class Meta():
        model = Userprofile
        fields = ('portfolio_site', 'profile_pic')
