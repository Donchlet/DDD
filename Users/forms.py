from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from . import models


class RegistrationForm(UserCreationForm):
    MALE = 1
    FEMALE = 2
    OTHER = 3
    GENDER_TYPE = (
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other")
    )
    OCUP_CHOICE = (
        ("STUDENT", "STUDENT"),
        ("WORKER", "WORKER"),
        ("JOBLESS", "JOBLESS"),
        ("RETIRED", "RETIRED"),
        ("MILLIONAIRE", "MILLIONAIRE")
    )
    email = forms.EmailField(required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    occupation = forms.ChoiceField(choices=OCUP_CHOICE, required=True)

    class Meta:
        model = models.CustomUser
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "age",
            "gender",
            "occupation",
            "phone_number",
            "mothers_maiden_name",
            "best_friend_name",
            "place_of_residence",
            "favorite_song",
            "first_book"
        ]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "username",
                "id": "username"
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "type password",
                "id": "password"
            }
        )
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "email",
                "id": "email"
            }
        )
    )

    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "phone_number",
                "id": "phone_number"
            }
        )
    )