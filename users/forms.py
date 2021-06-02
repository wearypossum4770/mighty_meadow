from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField, ModelForm

from .models import Profile

User = get_user_model()


class UserRegisterForm(UserCreationForm):
    email = EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class UserUpdateForm(ModelForm):
    email = EmailField()

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
        )


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = (
            "image",
            "addresses",
        )
