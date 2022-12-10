from django.shortcuts import HttpResponseRedirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from .models import AbstractUserModel
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class RegistrationFormView(TemplateView):
    template_name = "authapp/register.html"

    def post(self, request, *args, **kwargs):
        try:
            if all(
                (
                    request.POST.get("email"),
                    request.POST.get("password1"),
                    request.POST.get(
                        "password1") == request.POST.get("password2"),
                )
            ):
                new_user = AbstractUserModel.objects.create(
                    email=request.POST.get("email"),

                )
                new_user.set_password(request.POST.get("password1"))
                new_user.save()
            return HttpResponseRedirect(reverse_lazy("authapp:login"))
        except Exception as exp:
            messages.add_message(
                request,
                messages.WARNING,
            )
            return HttpResponseRedirect(reverse_lazy("authapp:register"))
