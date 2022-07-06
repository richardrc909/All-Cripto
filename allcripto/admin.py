from django.contrib import admin
from .models import Bitcoin, Ethereum, MetaVerse, Tutorial, Prices, Business

@admin.register(Bitcoin)
class AuthorAdmin(admin.ModelAdmin):
    pass