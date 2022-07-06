from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Bitcoin, Ethereum

class BitcoinNews(TemplateView):
    template_name = 'allcripto/bitcoin.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['bitcoin_news'] = Bitcoin.objects.all()
        return context

class BitcoinDetail(DetailView):
    model = Bitcoin
    template_name = 'allcripto/bitcoin_detail.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = Bitcoin.objects.filter(slug=self.kwargs.get('slug'))
        return context