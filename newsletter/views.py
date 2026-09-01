from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import FormView

from .forms import SubscriberForm
from .models import Subscriber


class SubscribeView(FormView):

    form_class = SubscriberForm

    template_name = "newsletter/subscribe.html"

    success_url = "/"

    def form_valid(self, form):

        email = form.cleaned_data["email"]

        subscriber, created = Subscriber.objects.get_or_create(
            email=email,
            defaults={
                "name": form.cleaned_data.get(
                    "name",
                    ""
                ),
                "is_active": True,
            },
        )

        if not created:

            subscriber.name = form.cleaned_data.get(
                "name",
                subscriber.name
            )

            subscriber.is_active = True

            subscriber.save()

        messages.success(
            self.request,
            "You're subscribed! Welcome to Code & Control."
        )

        return super().form_valid(form)

    def form_invalid(self, form):

        messages.error(
            self.request,
            "Please check your email address."
        )

        return redirect(
            self.request.META.get(
                "HTTP_REFERER",
                "/"
            )
        )