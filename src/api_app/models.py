from pathlib import Path

from django.db import models


class Upload(models.Model):
    caption = models.CharField(max_length=64, blank=True)
    image_file = models.ImageField(upload_to=Path("uploads/"))

    # owner = models.ForeignKey(
    #     "auth.User",
    #     related_name="uploads",
    #     on_delete=models.CASCADE,
    # )
