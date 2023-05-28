from cProfile import label
from django.core.exceptions import ValidationError 
from django import forms#ok
from django.contrib.auth.forms import UserCreationForm#ok
from django.contrib.auth.models import User#ok

# class SignUpForm(UserCreationForm):
    
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email']
#         labels = {'email': 'Email'}

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already taken. Please choose a different one.")
        return email