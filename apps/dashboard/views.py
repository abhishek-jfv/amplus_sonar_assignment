import csv

from django.db import transaction
from rest_framework import generics
from rest_framework.response import Response

from apps.dashboard.models import SolarPlant, SolarPlantReading
from apps.dashboard.serializers import DashboardStatViewSerializer


class DashboardStatView(generics.GenericAPIView):
    def get(self, request, solar_plant_uid):
        # self.seed_db_from_csv()
        start_date = request.query_params["start_date"]
        end_date = request.query_params["end_date"]
        solar_plant = SolarPlant.objects.filter(uid=solar_plant_uid).first()
        solar_plant_readings = SolarPlantReading.objects.filter(
            solar_plant=solar_plant,
            reading_date__gte=start_date,
            reading_date__lte=end_date
        )
        solar_plant_readings_serializer = DashboardStatViewSerializer(solar_plant_readings, many=True)
        return Response(solar_plant_readings_serializer.data)

    def seed_db_from_csv(self):
        SolarPlant.objects.all().delete()
        raw_data_filepath = "data/RawData.csv"
        solar_plant_reading_data = []
        raw_data_file = open(raw_data_filepath, 'r')
        fieldnames = ("solar_plant", "reading_date", "reading_type", "reading_value")
        reader = csv.DictReader(raw_data_file, fieldnames)
        next(reader, None)
        for row in reader:
            solar_plant_reading_data.append(row)
        plant_ids = list(set([x["solar_plant"] for x in solar_plant_reading_data]))
        with transaction.atomic():
            for id in plant_ids:
                SolarPlant.objects.get_or_create(uid=id)
            solar_plants = SolarPlant.objects.all()
            for row in solar_plant_reading_data:
                row["solar_plant"] = solar_plants.filter(uid=row["solar_plant"]).first()
                if row["solar_plant"]:
                    SolarPlantReading.objects.get_or_create(**row)
