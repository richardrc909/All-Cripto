from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.utils import timezone

class Bitcoin(models.Model):
    title = models.TextField()
    header = models.TextField()
    paragraph = models.TextField()
    slug = AutoSlugField(max_length=250, populate_from = 'title', null=True, unique=True)
    extracted_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title + ' ' + self.header + ' ' + self.paragraph

class Ethereum(models.Model):
    title = models.TextField()
    header = models.TextField()
    paragraph = models.TextField()
    slug = AutoSlugField(max_length=250, populate_from = 'title', null=True, unique=True)
    extracted_at = models.DateTimeField(default=timezone.now)

class MetaVerse(models.Model):
    title = models.TextField()
    header = models.TextField()
    paragraph = models.TextField()
    slug = AutoSlugField(max_length=250, populate_from = 'title', null=True, unique=True)
    extracted_at = models.DateTimeField(default=timezone.now)


class Tutorial(models.Model):
    title = models.TextField()
    header = models.TextField()
    paragraph = models.TextField()
    slug = AutoSlugField(max_length=250, populate_from = 'title', null=True, unique=True)
    extracted_at = models.DateTimeField(default=timezone.now)

class Prices(models.Model):
    title = models.TextField()
    header = models.TextField()
    paragraph = models.TextField()
    slug = AutoSlugField(max_length=250, populate_from = 'title', null=True, unique=True)
    extracted_at = models.DateTimeField(default=timezone.now)


class Business(models.Model):
    title = models.TextField()
    header = models.TextField()
    paragraph = models.TextField()
    slug = AutoSlugField(max_length=250, populate_from = 'title', null=True, unique=True)
    extracted_at = models.DateTimeField(default=timezone.now)

class AnchorNews(models.Model):
    anchor_bit = models.TextField()
    anchor_eth = models.TextField()
    anchor_meta = models.TextField()
    anchor_tutorial = models.TextField()
    anchor_prices = models.TextField()
    anchor_business = models.TextField()
