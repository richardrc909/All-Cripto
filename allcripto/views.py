from django.shortcuts import render
from .models import Bitcoin, BitcoinBody


def index(request):
    return render(request, "allcripto/index.html")


def bitcoin(request):
    #cambiar mañana a '-id' para que las nuevas noticias se muestren arriba
    bitcoin_list = Bitcoin.objects.all().order_by('id')
    return render(request, "allcripto/bitcoin.html", {
        "bitcoin_list" : bitcoin_list
    })

def bitcoin_link(request):
    bitcoin_item = BitcoinBody.objects.get(pk='bitcoinbody_id')
    return render(request, "allcripto/bitcoin_detail.html", {
        "bitcoin_item" : bitcoin_item
    })
