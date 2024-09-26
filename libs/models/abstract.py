from django.db import models


class TimestampedModel(models.Model):
    """Abstract model which adds creation and update timestamps."""

    class Meta:
        abstract = True

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
