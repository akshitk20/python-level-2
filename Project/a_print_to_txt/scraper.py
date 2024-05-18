import requests
from bs4 import BeautifulSoup

LOAD_DATA = False
DEBUG = True
URL = 'https://en.wikipedia.org/wiki/Member_states_of_the_United_Nations'

if LOAD_DATA:
    headers = {'User-Agent': f'Akshit Khatri (akshitkhatri.20@gmail.com)'}
    response = requests.get(URL, headers)

    #print(response.text)
    print(response.status_code)
    html_doc = response.text
    with open("Solutions/a_print_to_txt/countries.txt", 'w', encoding='utf-8') as countries:
        countries.write(html_doc)
else:
    with open("Solutions/a_print_to_txt/countries.txt", encoding='utf-8') as countries:
        html_doc = countries.read()

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify(formatter='html'))
table = soup.find('table', class_='wikitable')
rows = table.find_all('tr')
countries = []
for row in rows:
    th = row.th
    name_link = th.a
    #print(name_link)
    if name_link:
        name = name_link.text
        date_admitted = row.td.text
        countries.append(name)
        print(date_admitted)

#print(rows)
print(len(countries))

#with open("countries.txt", 'w') as file:
#    for country in countries:
#        file.write(country + "\n")
