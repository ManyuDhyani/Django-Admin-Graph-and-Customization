from urllib import request
from django.shortcuts import render
from .models import City
from django.db.models import Sum
from django.http import JsonResponse

def pie_chart(request):
    labels = []
    data = []

    queryset = City.objects.order_by('population')
    for city in queryset:
        labels.append(city.name)
        data.append(city.population)

    return render(request, 'pieChart.html', {
        'labels': labels,
        'data': data,
    })


def population_chart(request):
    labels = []
    data = []

    queryset = City.objects.values('country__name').annotate(country_population=Sum('population')).order_by('-country_population')
    for entry in queryset:
        labels.append(entry['country__name'])
        data.append(entry['country_population'])
    
    return render(request, 'populationChart.html', {
        'labels': labels,
        'data': data,
    })

def high_chart(request):
    return render(request, "highChart.html")