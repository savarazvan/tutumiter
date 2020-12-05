import requests
from bs4 import BeautifulSoup 
from django.shortcuts import render
from django.http import HttpResponse

from .countries import countries
from .models import Country

def country_list(request):
    return render(request, 'index.html', {'countries': Country.objects.all()})

def get_started(request):
    return render(request, 'form.html', {'countries': Country.objects.all()})

def country(request):
    return render(request, 'country.html')

def update_db(request):
    for c in countries:
        name = c
        c = c.lower()
        bs = BeautifulSoup(requests.get('https://travelbans.org/europe/'+ c ).text, 'html.parser')
        foreigners_status = bs.find('span', {'class': 'type-open_for_foreigners'})
        tourism_status = bs.find('span', {'class': 'type-open_for_tourism'})
        quarantine = bs.find('span', {'class': 'type-quarantine'})
        foreigners_status = foreigners_status['class']
        foreigners_status = foreigners_status[0]
        foreigners_status =  foreigners_status[7:]
        tourism_status = tourism_status['class']
        tourism_status = tourism_status[0]
        tourism_status = tourism_status[7:]
        quarantine = quarantine['class']
        quarantine = quarantine[0]
        quarantine = quarantine[7:]
        cntry = Country(name=name, open_for_f=foreigners_status, open_for_t=tourism_status, quarantine=quarantine)
        cntry.save()

    bs = BeautifulSoup(requests.get('https://travelbans.org/europe/'+ 'republic-of-ireland' ).text, 'html.parser')
    foreigners_status = bs.find('span', {'class': 'type-open_for_foreigners'})
    tourism_status = bs.find('span', {'class': 'type-open_for_tourism'})
    quarantine = bs.find('span', {'class': 'type-quarantine'})
    foreigners_status = foreigners_status['class']
    foreigners_status = foreigners_status[0]
    foreigners_status =  foreigners_status[7:]
    tourism_status = tourism_status['class']
    tourism_status = tourism_status[0]
    tourism_status = tourism_status[7:]
    quarantine = quarantine['class']
    quarantine = quarantine[0]
    quarantine = quarantine[7:]
    cntry = Country(name='Ireland', open_for_f=foreigners_status, open_for_t=tourism_status, quarantine=quarantine)
    cntry.save()

    bs = BeautifulSoup(requests.get('https://travelbans.org/europe/'+ 'czech-republic' ).text, 'html.parser')
    foreigners_status = bs.find('span', {'class': 'type-open_for_foreigners'})
    tourism_status = bs.find('span', {'class': 'type-open_for_tourism'})
    quarantine = bs.find('span', {'class': 'type-quarantine'})
    foreigners_status = foreigners_status['class']
    foreigners_status = foreigners_status[0]
    foreigners_status =  foreigners_status[7:]
    tourism_status = tourism_status['class']
    tourism_status = tourism_status[0]
    tourism_status = tourism_status[7:]
    quarantine = quarantine['class']
    quarantine = quarantine[0]
    quarantine = quarantine[7:]
    cntry = Country(name='Czechia', open_for_f=foreigners_status, open_for_t=tourism_status, quarantine=quarantine)
    cntry.save()
    
    return HttpResponse('kfjdkjashfklsd')