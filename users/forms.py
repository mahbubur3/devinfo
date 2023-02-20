from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile, Skill, Message


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

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'location', 'intro', 'bio', 'profile_picture', 'github', 'twitter', 'linkedin', 'youtube', 'facebook', 'website']

    # implement style in input form 
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'input'})
        self.fields['email'].widget.attrs.update({'class': 'input'})
        self.fields['username'].widget.attrs.update({'class': 'input'})
        self.fields['location'].widget.attrs.update({'class': 'input'})
        self.fields['intro'].widget.attrs.update({'class': 'input'})
        self.fields['bio'].widget.attrs.update({'class': 'input'})
        self.fields['profile_picture'].widget.attrs.update({'class': 'input'})
        self.fields['github'].widget.attrs.update({'class': 'input'})
        self.fields['twitter'].widget.attrs.update({'class': 'input'})
        self.fields['linkedin'].widget.attrs.update({'class': 'input'})
        self.fields['youtube'].widget.attrs.update({'class': 'input'})
        self.fields['facebook'].widget.attrs.update({'class': 'input'})
        self.fields['website'].widget.attrs.update({'class': 'input'})


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']

    # implement style in input form 
    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'input'})
        self.fields['description'].widget.attrs.update({'class': 'input'})


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']

    # implement style in input form 
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
