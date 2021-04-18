from django.db import models


class Click(models.Model):
    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ('-timestamp', )
