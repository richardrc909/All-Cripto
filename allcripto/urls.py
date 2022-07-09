from django.urls import path

from .views import BitcoinNews, BitcoinDetail, EthereumNews, EthereumDetail

app_name = 'allcripto'

urlpatterns = [
    path('bitcoin/', BitcoinNews.as_view() , name="bitcoin_news"),
    path('<slug:slug>/', BitcoinDetail.as_view(), name="bitcoin_detail")
]

urlpatterns = [
    path('ethereum/', EthereumNews.as_view(), name="ethereum_news"),
    path('<slug:slug>/', EthereumDetail.as_view(), name="ethereum_detail")
]
