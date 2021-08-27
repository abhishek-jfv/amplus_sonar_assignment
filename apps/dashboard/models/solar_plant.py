from django.db import models
from lib.model_mixins.timestamps import TimestampsModelMixin


class SolarPlant(TimestampsModelMixin):
    uid = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False
    )
