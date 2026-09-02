from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from accounts.models import StudentProfile


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


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile

        fields = [
            "phone",
            "bio",
            "profile_picture",
        ]

        widgets = {
            "phone": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Phone number",
                }
            ),

            "bio": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "placeholder": "Tell us a little about yourself...",
                    "rows": 5,
                }
            ),

            "profile_picture": forms.ClearableFileInput(
                attrs={
                    "class": "form-input",
                }
            ),
        }



class UserInformationForm(forms.ModelForm):

    class Meta:

        model = User

        fields = [
            "first_name",
            "last_name",
            "email",
        ]

        widgets = {

            "first_name": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "First name",
                }
            ),

            "last_name": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Last name",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Email address",
                }
            ),
        }