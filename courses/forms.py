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
                    "class": "form-input",
                    "placeholder": "Your full name",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Your email address",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Phone number (optional)",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "placeholder": "Tell us anything we should know...",
                    "rows": 5,
                }
            ),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        # Logged-in student
        if user and user.is_authenticated:

            full_name = user.get_full_name().strip()

            if not full_name:
                full_name = user.username

            self.fields["name"].initial = full_name
            self.fields["email"].initial = user.email

            # Prevent changing account details during enrollment
            self.fields["name"].disabled = True
            self.fields["email"].disabled = True