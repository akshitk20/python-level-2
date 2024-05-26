import requests
from bs4 import BeautifulSoup
import csv

LOAD_DATA = False
URL = 'https://www.flipkart.com/audio-video/headset/pr?sid=0pm%2Cfcn&p%5B%5D=facets.connectivity%255B%255D%3DBluetooth&sort=popularity&p%5B%5D=facets.rating%255B%255D%3D3%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.price_range.from%3D599&p%5B%5D=facets.price_range.to%3DMax&p%5B%5D=facets.headphone_type%255B%255D%3DTrue%2BWireless&param=86&hpid=WqCPtE2MbDEYEbYbttXC1qp7_Hsxr70nj65vMAAFKlc%3D&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJHcmFiIE5vdyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sImhlcm9QaWQiOnsic2luZ2xlVmFsdWVBdHRyaWJ1dGUiOnsia2V5IjoiaGVyb1BpZCIsImluZmVyZW5jZVR5cGUiOiJQSUQiLCJ2YWx1ZSI6IkFDQ0dNWlhTN1lLRVZLQTMiLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19LCJ0aXRsZSI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ0aXRsZSIsImluZmVyZW5jZVR5cGUiOiJUSVRMRSIsInZhbHVlcyI6WyJCZXN0IFRydWV3aXJlbGVzcyBIZWFkcGhvbmVzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&fm=neo%2Fmerchandising&iid=M_74bdc1e5-cd40-4ab3-9181-d72bb6ad8fab_1.KVOY5PS5484O&ppt=hp&ppn=homepage&ssid=tu9l69j2g00000001716726734463&otracker=dynamic_omu_infinite_Best%2Bof%2BElectronics_2_1.dealCard.OMU_INFINITE_KVOY5PS5484O&cid=KVOY5PS5484O'

if LOAD_DATA:
    response = requests.get(URL)
    print(response.status_code)
    html_doc = response.text
    with open('data/flipkart-electronics.html', 'w') as file:
        file.write(html_doc)
else:
    with open('data/flipkart-electronics.html') as file:
        html_doc = file.read()

soup = BeautifulSoup(html_doc, 'html.parser')

electronics = soup.find_all('div', class_='_75nlfW')
print(electronics)
watches = []
for product in electronics:
    name = product.find('a', class_='wjcEIp').string
    description = product.find('div', class_='NqpwHC').string
    rating = product.find('div', class_='XQDdHH').string
    price = product.find('div', class_='Nx9bqj').string
    total_price = product.find('div', class_='yRaY8j').string
    discount = product.find('div', class_='UkUFwK').string
    watch = {
        "Name": name,
        "Description": description,
        "Rating": rating,
        "Price": price,
        "Total Price": total_price,
        "Discount": discount
    }
    watches.append(watch)

print(watches)

with open('data/flipkart-watches.txt', 'w') as file:
    writer = csv.DictWriter(file, fieldnames={'Name', 'Description', 'Rating', 'Price', 'Total Price', 'Discount'})
    writer.writeheader()
    writer.writerows(watches)
