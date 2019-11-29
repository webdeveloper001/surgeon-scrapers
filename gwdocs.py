# -*- coding: utf-8 -*-
import csv     
import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup 
import sys
reload(sys)
sys.setdefaultencoding('utf8')



csv.register_dialect('myDialect1',
	  quoting=csv.QUOTE_ALL,
	  skipinitialspace=True)

write_file = open('gwdocs.csv', 'a')
csv_writer = csv.writer(write_file, dialect='myDialect1')

csv_writer.writerow(['Name', 'Title', 'Specialties', 'Phone', 'Address'])

session = requests.Session()
session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    })
url = 'https://www.gwdocs.com/find-a-doctor/'
baseurl = 'https://www.gwdocs.com'
for page in range(1, 13):
    r = session.post(url, data={
        '_m_': 'PhysicianSearchResultsPanel',
        'PhysicianSearch$HDR0$SpecialtyIDs': '',
        'PhysicianSearch$HDR0$Gender': '',
        'PhysicianSearch$HDR0$PhysicianName': '',
        'PhysicianSearch$HDR0$City': '',
        'PhysicianSearch$HDR0$AffiliationIDs': '',
        'PhysicianSearch$HDR0$Position': '',
        'PhysicianSearch$HDR0$InterestIDs': '',
        'PhysicianSearch$HDR0$LastName': '',
        'PhysicianSearch$HDR0$Keywords': '',
        'PhysicianSearch$HDR0$ResultsPerPage': 50,
        'PhysicianSearch$HDR0$PagingID': page,
        'PhysicianSearch$FTR01$PagingID': page
    })
    soup = BeautifulSoup(r.text, features="html.parser")
    for doctor in soup.findAll('li', class_='phys-item'):
        name = doctor.find('div', class_='top').text.strip().split(',')[0]
        title = ''
        if len(doctor.find('div', class_='top').text.strip().split(',')) > 1:
            title = doctor.find('div', class_='top').text.strip().split(',')[1]
        detail = doctor.find('div', class_='top').find('a').attrs['href']
        speciality = ''
        for spec in doctor.find('ul', class_='specialty-list').findAll('li'):
            speciality = speciality + spec.text.strip() + ', '
        r = session.get(baseurl + detail)
        soup = BeautifulSoup(r.text, features="html.parser")
        phone = ''
        if soup.find('div', class_='book-phone') and soup.find('div', class_='book-phone').find('a'):
            phone = soup.find('div', class_='book-phone').find('a').text
            address = ''
        if soup.find('ul', class_='location-list'):
            address = " ".join(soup.find('ul', class_='location-list').find('p').text.strip().split())
        print(name, title, speciality[0:-2], phone, address)
        csv_writer.writerow([name, title, speciality[0:-2], phone, address])