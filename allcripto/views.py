from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Bitcoin, Ethereum, MetaVerse, Tutorial, Prices, Business

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


class EthereumNews(TemplateView):
    template_name = 'allcripto/ethereum.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ethereum_news'] = Ethereum.objects.all()
        return context

class EthereumDetail(DetailView):
    model = Ethereum
    template_name = 'allcripto/ethereum_detail.html'
    context_object_name = 'news_eth'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = Ethereum.objects.filter(slug=self.kwargs.get('slug'))
        return context