from urllib import request
from django.shortcuts import HttpResponseRedirect, render
from django.views.generic import View, TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404
from .models import CardsModel, HistoryCardModel
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin


def card_deactivate(request, pk):
    try:
        card = CardsModel.objects.get(id=pk)

        if request.method == "POST":
            card.status = "DEACTIVATE"
            card.save()
            return HttpResponseRedirect(f"/card/{pk}")
    except CardsModel.DoesNotExist:
        return HttpResponseRedirect("/")


def card_activate(request, pk):
    try:
        card = CardsModel.objects.get(id=pk)

        if request.method == "POST":
            card.status = "ACTIVATE"
            card.save()
            return HttpResponseRedirect(f"/card/{pk}")
    except CardsModel.DoesNotExist:
        return HttpResponseRedirect("/")


class CardsView(TemplateView):
    template_name = "app/index.html"

    def get_context_data(self, **kwargs):
        context = super(CardsView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user'] = self.request.user.id
            context['cards'] = CardsModel.objects.filter(user=context['user'])
        return context


class CardDetailView(TemplateView):
    template_name = "app/card_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['card_object'] = get_object_or_404(
            CardsModel, pk=pk
        )
        context['history_card'] = HistoryCardModel.objects.filter(
            card=context['card_object'])
        return context


class CardDeleteView(DeleteView):
    model = CardsModel
    success_url = reverse_lazy("app:cards")
    permission_required = ("app:delete_card",)
