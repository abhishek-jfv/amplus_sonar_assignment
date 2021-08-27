from rest_framework import serializers

from apps.dashboard.models import SolarPlantReading


class DashboardStatViewSerializer(serializers.ModelSerializer):
    solar_plant_id = serializers.SerializerMethodField()
    solar_plant_uid = serializers.SerializerMethodField()

    class Meta:
        model = SolarPlantReading
        fields = [
            'id',
            'solar_plant_id',
            'solar_plant_uid',
            'reading_date',
            'reading_type',
            'reading_value',
        ]

    def get_solar_plant_id(self, obj):
        return obj.solar_plant.id

    def get_solar_plant_uid(self, obj):
        return obj.solar_plant.uid
