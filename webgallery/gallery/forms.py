from django import forms
from gallery.models import UserProfile, Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
        )


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic',)


class UserPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'post_img')


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'username',
            'password',
        )
