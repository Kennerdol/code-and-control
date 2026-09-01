from django import forms

from .models import Subscriber


class SubscriberForm(forms.ModelForm):

    class Meta:

        model = Subscriber

        fields = [
            "name",
            "email",
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "placeholder": "Your name",
                    "class": "newsletter-input",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Your email address",
                    "class": "newsletter-input",
                }
            ),
        }

    def clean_email(self):

        email = self.cleaned_data["email"].strip().lower()

        if Subscriber.objects.filter(
            email=email,
            is_active=True,
        ).exists():

            raise forms.ValidationError(
                "This email is already subscribed."
            )

        return email