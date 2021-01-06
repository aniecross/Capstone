from django import forms
from authentication.models import SignUp


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = '__all__'
        widgets = {
        'password' : forms.PasswordInput(), 
        }