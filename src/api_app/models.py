from django.db import models


class ImageStorage(models.Model):
    caption = models.CharField(max_length=64, blank=True)
    file_ = models.ImageField(...)
