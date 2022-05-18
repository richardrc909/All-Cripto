from django.db import models

class Bitcoin(models.Model):
    title = models.TextField()
    header = models.TextField()

    def __str__(self) -> str:
        return self.title


class BitcoinBody(models.Model):
    paragraph = models.TextField()

    def __str__(self) -> str:
        return self.paragraph
