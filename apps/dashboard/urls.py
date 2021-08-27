from django.urls import path
from . import views

urlpatterns = [
    path('stats/solar_plant/<slug:solar_plant_uid>', views.DashboardStatView.as_view())
]
