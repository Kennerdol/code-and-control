from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Your email address",
                "class": "form-input",
            }
        ),
    )

    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "First name",
                "class": "form-input",
            }
        ),
    )

    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last name",
                "class": "form-input",
            }
        ),
    )

    class Meta:

        model = User

        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]

    def clean_email(self):

        email = self.cleaned_data["email"].strip().lower()

        if User.objects.filter(
            email__iexact=email
        ).exists():

            raise forms.ValidationError(
                "An account with this email already exists."
            )

        return email



class LoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-input",
            }
        ),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-input",
            }
        ),
    )