import requests
from bs4 import BeautifulSoup
import csv

LOAD_DATA = True
BASE_URL = 'https://www.flipkart.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

if LOAD_DATA:
    response = requests.get(BASE_URL,headers)

    print(response.text)
    html_doc = response.text
    with open('data/flipkart.html', 'w') as flipkart:
        flipkart.write(html_doc)

else:
    with open('data/flipkart.html') as flipkart:
        html_doc = flipkart.read()

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify(formatter='html'))
#observer_id_value = 'a5612b34-f7a6-4024-bc9e-b83ce31bd616'
#electronics = soup.find('div', class_='css-175oi2r')
#electronics = soup.find('div', attrs={'data-observerid-7da0ea20-c334-4213-95bb-a04cee82e0d9': observer_id_value})
#print(electronics)
#child_divs = electronics.find_all('div')
#for index, child_div in enumerate(child_divs):
#    print(f'Child div {index+1}')
#    print(child_divs)
