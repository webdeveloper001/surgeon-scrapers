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

write_file = open('surgeon_sample.csv', 'a')
csv_writer = csv.writer(write_file, dialect='myDialect1')

csv_writer.writerow(['FirstName', 'LastName', 'Phone', 'Email', 'Website', 'State', 'City'])

session = requests.Session()

session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Cookie': 'ASP.NET_SessionId=eevku0jy3nzxfhbpdr4yyy1m; AWSELB=89E98DE91A106794F0B5F25D2ED9805051C8EB8863936EC1B86F446230FD1BC232DF99DCBE40CB8088AAECDACF99EE627AAD79B23E7B1F1CBE290C18584AFDCFF75F8BA01F; _ga=GA1.2.44013263.1567724958; _gid=GA1.2.1887320606.1567724958; __utma=169201760.44013263.1567724958.1567724959.1567724959.1; __utmc=169201760; __utmz=169201760.1567724959.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __ss=1567724959477; __ss_tk=201909%7C5d7195a0313ab7074f66ee45; __adroll_fpc=d664880652be9f516a7704337e287b11-s2-1567724963276; _vwo_uuid_v2=D044F18E435AF5B4F466C1F9B6F046AFB|1d3ab8e0eeecc03b88ad07671ca6691b; _fbp=fb.1.1567725451248.1268389080; __utmt=1; __ss_referrer=https%3A//find.plasticsurgery.org/default.aspx%3Fprocs%3D23-24%26page%3D2; __ar_v4=I7CJRKFZKFCN5AGATJQ2T5%3A20190905%3A11%7CW3KGBEO7ZZFLVHH7I2QTFH%3A20190905%3A11%7CPYQUKAN3TZGLPADU2XBOYY%3A20190905%3A11; __utmb=169201760.20.9.1567725632761'
})
session1 = requests.Session()
session1.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'sec-fetch-site': 'same-site',
                'upgrade-insecure-requests': '1',
                'Cookie': '_ga=GA1.2.44013263.1567724958; _gid=GA1.2.1887320606.1567724958; __utma=169201760.44013263.1567724958.1567724959.1567724959.1; __utmc=169201760; __utmz=169201760.1567724959.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); IGXSessionState=1hayvuolckbn1wdgchihlbij; __ss=1567725449704; __ss_tk=201909%7C5d7195a0313ab7074f66ee45; _vwo_uuid_v2=D044F18E435AF5B4F466C1F9B6F046AFB|1d3ab8e0eeecc03b88ad07671ca6691b; _fbp=fb.1.1567725451248.1268389080; __adroll_fpc=c2c02fd1dd7efc5d1eac4b6105893452-s2-1567725453426; __ss_referrer=https%3A//www.plasticsurgery.org/md/tjhubbard.html; __utmt=1; __atuvc=6%7C36; __atuvs=5d71978a0f71d483005; __ar_v4=I7CJRKFZKFCN5AGATJQ2T5%3A20190905%3A3%7CW3KGBEO7ZZFLVHH7I2QTFH%3A20190905%3A3%7CPYQUKAN3TZGLPADU2XBOYY%3A20190905%3A3; _gat=1; __utmb=169201760.48.9.1567727148457'
            })

session2 = requests.Session()
session2.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'XMLHttpRequest',
                'origin': 'https://find.plasticsurgery.org',
                'content-type': 'application/json; charset=UTF-8',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'Cookie': '_ga=GA1.2.44013263.1567724958; _gid=GA1.2.1887320606.1567724958; __ss_tk=201909%7C5d7195a0313ab7074f66ee45; __adroll_fpc=d664880652be9f516a7704337e287b11-s2-1567724963276; _vwo_uuid_v2=D044F18E435AF5B4F466C1F9B6F046AFB|1d3ab8e0eeecc03b88ad07671ca6691b; _fbp=fb.1.1567725451248.1268389080; __utmz=169201760.1567757542.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ASP.NET_SessionId=0axtgfizcxavhzy0h1wbnpnf; AWSELB=89E98DE91A106794F0B5F25D2ED9805051C8EB8863936EC1B86F446230FD1BC232DF99DCBE40CB8088AAECDACF99EE627AAD79B23E7B1F1CBE290C18584AFDCFF75F8BA01F; __ss=1567786965536; __utmc=169201760; __utma=169201760.44013263.1567724958.1567786966.1567786966.3; __ss_referrer=https%3A//find.plasticsurgery.org/city/new-york/%3Fpage%3D21; _gat=1; __utmt=1; __ar_v4=I7CJRKFZKFCN5AGATJQ2T5%3A20190905%3A35%7CW3KGBEO7ZZFLVHH7I2QTFH%3A20190905%3A35%7CPYQUKAN3TZGLPADU2XBOYY%3A20190905%3A35; __utmb=169201760.29.9.1567792117542'
            })

url = 'https://find.plasticsurgery.org/'
r = session.get(url)
soup = BeautifulSoup(r.text, features="html.parser")
locationlist = soup.findAll('div', class_='panel')[0].findAll('a')

for location in locationlist:
    # print(location.attrs['href'])
    if 'javascript' in location.attrs['href']:
        loc = '/state/' + location.attrs['href'].replace("javascript:showCities('", '').split("',")[0]
    else:
        loc = location.attrs['href']
    print(loc)
    page = 1
    while page >= 1:
        url = 'https://find.plasticsurgery.org{}/?page=' + str(page)
        r = session.get(url.format(loc))
        soup = BeautifulSoup(r.text, features="html.parser")
        searchid = soup.find('input', {"id": 'hfSearchLogID'}).attrs['value']
        surgeons = soup.findAll('div', class_='resultSet')
        for surgeon in surgeons:
            detail = surgeon.find('td', class_='surgeonProfileBoxDescription')
            firstName = detail.find('h3').find('span').text.split(',')[0].split(' ')[0]
            lastName = detail.find('h3').find('span').text.split(',')[0].split(' ')[1]
            email = ''
            website = ''
            flag = True
            phone = ''
            phone = surgeon.findAll('p')[2].text.strip()
            address = surgeon.findAll('p')[0].text.strip().replace('  ', '')
            print(address)
            state = ''
            if len(address.split('\r\n')[2].split(', ')) > 1:
                state = address.split('\r\n')[2].split(', ')[1].split(' ')[0]
            city = address.split('\r\n')[2].split(', ')[0]
            if len(surgeon.findAll('tr')) > 1:
                if surgeon.findAll('tr')[1].find('a'):
                    flag = False
                    url = surgeon.findAll('tr')[1].find('a').attrs['href'].strip()
                    r = session1.get(url)
                    soup1 = BeautifulSoup(r.text, features="html.parser")
                    for contactinfo in soup1.find('div', class_='contact').findAll('a'):
                        if contactinfo.attrs['data-contact-type'] == 'Email':
                            email = contactinfo.text.strip()
                        if contactinfo.attrs['data-contact-type'] == 'PrimaryLink':
                            website = contactinfo.text.strip()
                        if contactinfo.attrs['data-contact-type'] == 'Phone':
                            phone = contactinfo.text.strip()
            if flag == True:
                memberid = surgeon.findAll('a', class_='ignore-click')[0].attrs['onclick'].replace("showMemberInfo('", '').replace("');", '')
                apiurl = 'https://find.plasticsurgery.org/default.aspx/GetMemberInfo'
                r = session2.post(apiurl, data = json.dumps({"searchId":searchid,"memberId":memberid}))
                detail = json.loads(r.text)
                website = detail['d']['Website']
                email = detail['d']['Email']
        #     # if detail.find('a', class_='enhancedBar'): 
        #         # print(detail.find('a', class_='enhancedBar').attrs['href'])
            

            csv_writer.writerow([firstName, lastName, phone, email, website, state, city])
            print(firstName, lastName, phone, email, website, state, city)
        pagination = soup.find('ul', class_='pagination').findAll('li')
        if 'class' in pagination[len(pagination) - 1].attrs:
            if pagination[len(pagination) - 1].attrs['class'][0] == 'disabled':
                break
        page = page + 1

write_file.close()