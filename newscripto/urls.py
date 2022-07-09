
from django.contrib import admin
from .views import HomePage
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name="home"),
    path('allcripto/', include('allcripto.urls', namespace='allcripto'))
]
