from django.db import models
from django.utils.translation import gettext_lazy as _

from lib.model_mixins.timestamps import TimestampsModelMixin
from apps.dashboard.models import SolarPlant


class SolarPlantReadingType(models.TextChoices):
    GENERATION = "generation", _("Generation")
    IRRADIATION = "irradiation", _("Irradiation")


class SolarPlantReading(TimestampsModelMixin):
    solar_plant = models.ForeignKey(
        SolarPlant,
        on_delete=models.CASCADE,
        related_name="readings"
    )

    reading_date = models.DateField(
        null=False,
        blank=False,
    )

    reading_type = models.CharField(
        max_length=255,
        choices=SolarPlantReadingType.choices,
    )

    reading_value = models.DecimalField(
        max_digits=15,
        decimal_places=11,
    )

    class Meta:
        unique_together = [
            ['solar_plant', 'reading_date', 'reading_type'],
        ]
