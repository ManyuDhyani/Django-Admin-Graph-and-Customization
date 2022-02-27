from django.urls import path
from .views import pie_chart

app_name = 'Graphs'

urlpatterns = [
    path('pie-chart/', pie_chart, name='pie-chart'),
]