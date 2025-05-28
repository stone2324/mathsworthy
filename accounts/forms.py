from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        required=True,
    )
    email = forms.EmailField(
        required=True,
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove default help text for password fields
        self.fields['username'].help_text = ''
        self.fields['email'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('theme_preference', 'difficulty_level', 'notifications_enabled')
        widgets = {
            'theme_preference': forms.Select(choices=[
                ('light', 'Light'),
                ('dark', 'Dark'),
            ]),
            'difficulty_level': forms.Select(choices=[
                ('easy', 'Easy'),
                ('medium', 'Medium'),
                ('hard', 'Hard'),
            ]),
        } 