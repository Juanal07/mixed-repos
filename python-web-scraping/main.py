import os
import re

import requests
from bs4 import BeautifulSoup

URL = 'https://votainteligente.cl/propuestas/?page=9'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='posts')
job_elems = results.find_all('div', class_='post')

for job_elem in job_elems:
    category = job_elem.find('a')['href']
    category = re.search("clasification=(.*)", category)
    category = category.group(1)
    # print('Categoria: '+category)
    title = job_elem.find('h4')
    title = title.text
    title = re.sub("/", "-", title)
    # print('Titulo: '+title)
    leer_mas = job_elem.find('a', class_='btn btn-blue pull-right')['href']
    URL = 'https://votainteligente.cl' + leer_mas
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    cuerpo = soup.find('div', class_='col-md-12')
    cuerpo = cuerpo.find('p')
    if None:
        continue
    cuerpo = cuerpo.text
    # print('Cuerpo: ' + cuerpo)
    # print()
    if not os.path.exists('./dataset/' + category):
        os.makedirs('./dataset/' + category)
    f = open('./dataset/' + category + '/' + title, "w+")
    f.write(cuerpo)
    f.close()
