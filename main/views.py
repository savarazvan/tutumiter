import requests
from bs4 import BeautifulSoup 
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .countries import countries
from .models import Country, Atraction


def country_list(request):
    return render(request, 'index.html', {'countries': Country.objects.all()})

def get_started(request):
    return render(request, 'form.html', {'countries': Country.objects.all()})

def country(request, country):
    c = Country.objects.get(name=country)
    dictionary = {
       'country': c,
       'countries': Country.objects.all(),
       'attractions': Atraction.objects.filter(country=c)
    } 
    return render(request, 'country.html', dictionary)

@login_required
def create_db(request):
    for c in countries:
        print(c)
        name = c
        c = c.lower()
        bs = BeautifulSoup(requests.get('https://travelbans.org/europe/'+ c ).text, 'html.parser')
        foreigners_status = bs.find('span', {'class': 'type-open_for_foreigners'})
        tourism_status = bs.find('span', {'class': 'type-open_for_tourism'})
        quarantine = bs.find('span', {'class': 'type-quarantine'})
        advices = bs.findAll('td', {'class': 'the_content'})
        print('///')
        foreigners_status = foreigners_status['class']
        foreigners_status = foreigners_status[0]
        foreigners_status =  foreigners_status[7:]
        tourism_status = tourism_status['class']
        tourism_status = tourism_status[0]
        tourism_status = tourism_status[7:]
        quarantine = quarantine['class']
        quarantine = quarantine[0]
        quarantine = quarantine[7:]
        cntry = Country(name=name, open_for_f=foreigners_status, open_for_t=tourism_status, quarantine=quarantine, advices=advices)
        cntry.save()

    bs = BeautifulSoup(requests.get('https://travelbans.org/europe/'+ 'republic-of-ireland' ).text, 'html.parser')
    foreigners_status = bs.find('span', {'class': 'type-open_for_foreigners'})
    tourism_status = bs.find('span', {'class': 'type-open_for_tourism'})
    quarantine = bs.find('span', {'class': 'type-quarantine'})
    advices = bs.find('td', {'class': 'the_content'})
    advices = advices.text
    foreigners_status = foreigners_status['class']
    foreigners_status = foreigners_status[0]
    foreigners_status =  foreigners_status[7:]
    tourism_status = tourism_status['class']
    tourism_status = tourism_status[0]
    tourism_status = tourism_status[7:]
    quarantine = quarantine['class']
    quarantine = quarantine[0]
    quarantine = quarantine[7:]
    cntry = Country(name='Ireland', open_for_f=foreigners_status, open_for_t=tourism_status, quarantine=quarantine, advices=advices)
    cntry.save()

    bs = BeautifulSoup(requests.get('https://travelbans.org/europe/'+ 'czech-republic' ).text, 'html.parser')
    foreigners_status = bs.find('span', {'class': 'type-open_for_foreigners'})
    tourism_status = bs.find('span', {'class': 'type-open_for_tourism'})
    quarantine = bs.find('span', {'class': 'type-quarantine'})
    advices = bs.find('td', {'class': 'the_content'})
    advices = advices.text
    foreigners_status = foreigners_status['class']
    foreigners_status = foreigners_status[0]
    foreigners_status =  foreigners_status[7:]
    tourism_status = tourism_status['class']
    tourism_status = tourism_status[0]
    tourism_status = tourism_status[7:]
    quarantine = quarantine['class']
    quarantine = quarantine[0]
    quarantine = quarantine[7:]
    cntry = Country(name='Czechia', open_for_f=foreigners_status, open_for_t=tourism_status, quarantine=quarantine, advices=advices)
    cntry.save()
    
    return HttpResponse('DataBase Create')

@login_required
def update_db(request):
    for c in countries:
        print(c)
        name = c
        c = c.lower()
        bs = BeautifulSoup(requests.get('https://travelbans.org/europe/'+ c ).text, 'html.parser')
        foreigners_status = bs.find('span', {'class': 'type-open_for_foreigners'})
        tourism_status = bs.find('span', {'class': 'type-open_for_tourism'})
        quarantine = bs.find('span', {'class': 'type-quarantine'})
        advices = bs.find('td', {'class': 'the_content'})
        print('///') 
        advices = advices.text
        if advices[-9:] == 'Read more':
            advices = advices[:-9]
        foreigners_status = foreigners_status['class']
        foreigners_status = foreigners_status[0]
        foreigners_status =  foreigners_status[7:]
        tourism_status = tourism_status['class']
        tourism_status = tourism_status[0]
        tourism_status = tourism_status[7:]
        quarantine = quarantine['class']
        quarantine = quarantine[0]
        quarantine = quarantine[7:]
        cntry = Country.objects.filter(name=name).update(open_for_f=foreigners_status, open_for_t=tourism_status, quarantine=quarantine, advices=advices)
       

    bs = BeautifulSoup(requests.get('https://travelbans.org/europe/'+ 'republic-of-ireland' ).text, 'html.parser')
    foreigners_status = bs.find('span', {'class': 'type-open_for_foreigners'})
    tourism_status = bs.find('span', {'class': 'type-open_for_tourism'})
    quarantine = bs.find('span', {'class': 'type-quarantine'})
    advices = bs.find('td', {'class': 'the_content'})
    advices = advices.text
    if advices[-9:] == 'Read more':
        advices = advices[:-9]
    foreigners_status = foreigners_status['class']
    foreigners_status = foreigners_status[0]
    foreigners_status =  foreigners_status[7:]
    tourism_status = tourism_status['class']
    tourism_status = tourism_status[0]
    tourism_status = tourism_status[7:]
    quarantine = quarantine['class']
    quarantine = quarantine[0]
    quarantine = quarantine[7:]
    cntry = Country.objects.filter(name='Ireland').update(open_for_f=foreigners_status, open_for_t=tourism_status, quarantine=quarantine, advices=advices)
    

    bs = BeautifulSoup(requests.get('https://travelbans.org/europe/'+ 'czech-republic' ).text, 'html.parser')
    foreigners_status = bs.find('span', {'class': 'type-open_for_foreigners'})
    tourism_status = bs.find('span', {'class': 'type-open_for_tourism'})
    quarantine = bs.find('span', {'class': 'type-quarantine'})
    advices = bs.find('td', {'class': 'the_content'})
    advices = advices.text
    if advices[-9:] == 'Read more':
        advices = advices[:-9]
    foreigners_status = foreigners_status['class']
    foreigners_status = foreigners_status[0]
    foreigners_status =  foreigners_status[7:]
    tourism_status = tourism_status['class']
    tourism_status = tourism_status[0]
    tourism_status = tourism_status[7:]
    quarantine = quarantine['class']
    quarantine = quarantine[0]
    quarantine = quarantine[7:]
    cntry = Country.objects.filter(name='Czechia').update(open_for_f=foreigners_status, open_for_t=tourism_status, quarantine=quarantine, advices=advices)
    
    
    return HttpResponse('DataBase Updated')