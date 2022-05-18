from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('bitcoin', views.bitcoin, name="bitcoin"),
    path('detail', views.bitcoin_link, name="bitcoin_detail")
]