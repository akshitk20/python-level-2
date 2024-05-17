import requests
from bs4 import BeautifulSoup
import csv

LOAD_DATA = False
DEBUG = True
BASE_URL = 'https://en.wikipedia.org'
URL = BASE_URL + '/wiki/Member_states_of_the_United_Nations'

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
        admitted_date = row.td.span.string  # row.td.span.string row.td.text
        country = {
            "Name": name,
            "Date Admitted": admitted_date,
            "URL": BASE_URL + name_link['href']
        }
        countries.append(country)
        #print(admitted_date)
#print(rows)
print(len(countries))

for country in countries[:2]:
    response = requests.get(country['URL'])
    if response.status_code != 200:
        print(f"Error on {country['URL']}, {response.status_code} , {response.reason}")
        continue
    html_doc = response.text
    soup = BeautifulSoup(html_doc, "html.parser")
    country['Latitude'] = soup.find('span', class_='latitude').string
    country['Longitude'] = soup.find('span', class_='longitude').string
print(countries)


#with open("countries.txt", 'w') as file:
#    for country in countries:
#        file.write(country + "\n")

with open("countries_added.csv", 'w') as file:
    writer = csv.DictWriter(file, fieldnames=('Name', "Date Admitted", "Latitude", "Longitude", 'URL'))
    writer.writeheader()
    writer.writerows(countries)
