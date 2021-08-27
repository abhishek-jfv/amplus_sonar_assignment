# Generated by Django 3.2.6 on 2021-08-27 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SolarPlant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uid', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SolarPlantReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('reading_date', models.DateField()),
                ('reading_type', models.CharField(choices=[('generation', 'Generation'), ('irradiation', 'Irradiation')], max_length=255)),
                ('reading_value', models.DecimalField(decimal_places=11, max_digits=15)),
                ('solar_plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='readings', to='dashboard.solarplant')),
            ],
            options={
                'unique_together': {('solar_plant', 'reading_date', 'reading_type')},
            },
        ),
    ]