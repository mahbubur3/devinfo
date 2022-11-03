from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name'
        }

    # implement style in input form 
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({'class': 'input'})
        self.fields['email'].widget.attrs.update({'class': 'input'})
        self.fields['username'].widget.attrs.update({'class': 'input'})
        self.fields['password1'].widget.attrs.update({'class': 'input'})
        self.fields['password2'].widget.attrs.update({'class': 'input'})

    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'location', 'intro', 'bio', 'profile_picture', 'github', 'twitter', 'linkedin', 'youtube', 'facebook', 'website']
