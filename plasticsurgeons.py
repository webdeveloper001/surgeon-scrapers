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

write_file = open('plasticsurgeons.csv', 'a')
csv_writer = csv.writer(write_file, dialect='myDialect1')

csv_writer.writerow(['FirstName', 'LastName', 'Phone', 'Email', 'Website', 'State', 'City'])

session = requests.Session()
session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    })


url = 'https://www.plasticsurgeons.com/local/pennsylvania/philadelphia?radius=25'
r = session.get(url)
soup = BeautifulSoup(r.text, features="html.parser")
cities = soup.findAll('a', class_='local-top-city-link2')
total = 0
city = cities[0]
print(city.attrs['href'].split('/'))
state = city.attrs['href'].split('/')[2].replace('-', '+')
cityname = city.attrs['href'].split('/')[3].split('?')[0].replace('-', '+')

session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
})
url = 'https://www.plasticsurgeons.com' + city.attrs['href']
r = session.get(url)

for page in range(0,5):
    url = 'https://www.plasticsurgeons.com/services/search/doctors/{}/10?includeFeatured=1'
    r = session.get(url.format(page + 1))
    # soup = BeautifulSoup(r.text, features="html.parser")
    doctors = json.loads(r.text)['Doctors']
    for doctor in doctors:
        url = 'https://www.plasticsurgeons.com/doctor/' + doctor['url_slug'] + '-' + doctor['doctor_id']
        r = session.get(url)
        soup = BeautifulSoup(r.text, features="html.parser")
        website = soup.find('a', class_='doctor-web').attrs['href'].replace('/doctor/webjump/?next=', '').split('&doctor_id')[0]
        print(doctor['first_name'], doctor['last_name'], doctor['phone'], '', website, doctor['state_name'], doctor['city'])
        csv_writer.writerow([doctor['first_name'], doctor['last_name'], doctor['phone'], '', website, doctor['state_name'], doctor['city']])
    # print(doctors['TotalResults'])
print(total)