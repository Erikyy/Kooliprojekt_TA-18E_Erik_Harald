from django import forms
from gallery.models import UserProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))

    password = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))

    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic',)
