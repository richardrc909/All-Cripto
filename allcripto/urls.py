from django.urls import path

from .views import BitcoinNews, BitcoinDetail, EthereumNews, EthereumDetail

app_name = 'allcripto'

urlpatterns = [
    path('bitcoin/', BitcoinNews.as_view() , name="bitcoin_news"),
    path('ethereum/', EthereumNews.as_view(), name="ethereum_news"),
    path('<slug:slug>/', BitcoinDetail.as_view(), name="bitcoin_detail"),
    path('<slug:slug>/', EthereumDetail.as_view(), name="ethereum_detail")
]

