from django.db import models


class Note(models.Model):
    title = models.CharField(
        max_length=60,
        blank=True
    )
    body = models.CharField(
        max_length=255
    )
    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ('-timestamp', )
