from django.urls import path

from .views import BitcoinNews, BitcoinDetail

app_name = 'allcripto'

urlpatterns = [
    path('bitcoin', BitcoinNews.as_view() , name="bitcoin_news"),
    path('<slug:slug>/', BitcoinDetail.as_view(), name="bitcoin_detail")
]