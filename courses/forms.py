from django import forms

from .models import Enrollment


class EnrollmentForm(forms.ModelForm):

    class Meta:

        model = Enrollment

        fields = [
            "name",
            "email",
            "phone",
            "message",
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "placeholder": "Your full name",
                    "class": "form-input",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Your email address",
                    "class": "form-input",
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "placeholder": "Phone number",
                    "class": "form-input",
                }
            ),

            "message": forms.Textarea(
                attrs={
                    "placeholder": (
                        "Tell me a little about yourself "
                        "and what you want to learn."
                    ),
                    "class": "form-input",
                    "rows": 5,
                }
            ),
        }