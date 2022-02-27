from django.urls import path
from .views import pie_chart, population_chart

app_name = 'Graphs'

urlpatterns = [
    path('pie-chart/', pie_chart, name='pie-chart'),
    path('population-chart/', population_chart, name='population-chart'),
]