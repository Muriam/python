from django.db import models


class Dictionary(models.Model):
    word = models.CharField(max_length=50)
    translation = models.CharField(max_length=50)

