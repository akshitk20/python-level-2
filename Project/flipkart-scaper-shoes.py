import requests
from bs4 import BeautifulSoup
import csv

LOAD_DATA = False
BASE_URL = 'https://www.flipkart.com/mens-footwear/pr?sid=osp%2Ccil&p%5B%5D=facets.brand%255B%255D%3DWOODLAND&p%5B%5D=facets.brand%255B%255D%3DCROCS&p%5B%5D=facets.brand%255B%255D%3DRED%2BCHIEF&p%5B%5D=facets.brand%255B%255D%3DRED%2BTAPE&p%5B%5D=facets.brand%255B%255D%3DHUSH%2BPUPPIES&p%5B%5D=facets.brand%255B%255D%3DRoadster&p%5B%5D=facets.brand%255B%255D%3DNAUTICA&p%5B%5D=facets.brand%255B%255D%3DJACK%2B%2526%2BJONES&p%5B%5D=facets.brand%255B%255D%3DFLYING%2BMACHINE&p%5B%5D=facets.brand%255B%255D%3DBata&p%5B%5D=facets.brand%255B%255D%3DU.S.%2BPOLO%2BASSN.&p%5B%5D=facets.brand%255B%255D%3DREEBOK%2BCLASSICS&p%5B%5D=facets.brand%255B%255D%3DADIDAS%2BORIGINALS&p%5B%5D=facets.brand%255B%255D%3DConverse&p%5B%5D=facets.brand%255B%255D%3DKILLER&p%5B%5D=facets.brand%255B%255D%3DLOUIS%2BPHILIPPE&p%5B%5D=facets.discount_range_v1%255B%255D%3D40%2525%2Bor%2Bmore&param=4&hpid=fqtpEbA_9-us6jGVani7Yap7_Hsxr70nj65vMAAFKlc%3D&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJNaW4uIDQwJSBPZmYiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19LCJoZXJvUGlkIjp7InNpbmdsZVZhbHVlQXR0cmlidXRlIjp7ImtleSI6Imhlcm9QaWQiLCJpbmZlcmVuY2VUeXBlIjoiUElEIiwidmFsdWUiOiJTSE9HWVVBNVhVQlI3RFJEIiwidmFsdWVUeXBlIjoiU0lOR0xFX1ZBTFVFRCJ9fSwidGl0bGUiOnsibXVsdGlWYWx1ZWRBdHRyaWJ1dGUiOnsia2V5IjoidGl0bGUiLCJpbmZlcmVuY2VUeXBlIjoiVElUTEUiLCJ2YWx1ZXMiOlsiVS5TLiBQb2xvIEFzc24uLCBIaWdobGFuZGVyLi4iXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19'

if LOAD_DATA:
    response = requests.get(BASE_URL, headers)

    print(response.text)
    html_doc = response.text
    with open('data/flipkart.html', 'w') as flipkart:
        flipkart.write(html_doc)

else:
    with open('data/flipkart.html') as flipkart:
        html_doc = flipkart.read()

soup = BeautifulSoup(html_doc, 'html.parser')
products = soup.find_all('div', class_='hCKiGj')
print(products)
shoes = []
for product in products:
    name = product.find('div', class_='syl9yP').string
    price = product.find('div', class_='Nx9bqj').string
    original_price = product.find('div', class_='yRaY8j').string
    discount = product.find('div', class_='UkUFwK').string
    title = product.find('a', class_='WKTcLC').string
    shoe = {
        "Name": name,
        "Title": title,
        "Original Price": original_price,
        "Final Price": price,
        "Discount": discount
    }
    shoes.append(shoe)

print(shoes)

with open('data/flipkart-shoes.txt', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=('Name', 'Title', 'Original Price', 'Final Price', 'Discount'))
    writer.writeheader()
    writer.writerows(shoes)
