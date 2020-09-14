from django import forms
from gallery.models import UserProfile, Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from crispy_forms.helper import FormHelper, Layout


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.wrapper_class = 'row'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'


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
        password = forms.CharField()
        fields = (
            'email',
            'first_name',
            'username',
            'password',
        )


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
        )
