from urllib import request
from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404
from .models import CardsModel, HistoryCardModel


class CardsView(TemplateView):
    template_name = "app/index.html"

    def get_context_data(self, **kwargs):
        context = super(CardsView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user'] = self.request.user
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
