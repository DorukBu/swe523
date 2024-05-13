from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models


class UserCreateForm(UserCreationForm):
    # profile_pic = forms.ImageField(required=False)  # Add profile_pic field
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"

class UserProfileInfoForm(forms.ModelForm):
    picture = forms.ImageField(required=False)

    class Meta():
        model = models.UserProfileInfo
        fields = ('profile_pic',)