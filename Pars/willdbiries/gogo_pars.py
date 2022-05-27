import lxml
import useragent
import requests
from bs4 import BeautifulSoup
from time import sleep
url = 'https://www.wildberries.ru/catalog/0/search.aspx?search=%D1%84%D1%83%D1%82%D0%B1%D0%BE%D0%BB%D0%BA%D0%B0%20%D0%B6%D0%B5%D0%BD%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%B9%D0%B7'
# response = requests.get('https://www.ozon.ru/category/knigi-16500/?category_was_predicted=true&text=%D0%BC%D0%B0%D1%80%D0%BA%D1%81')

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
}

result = requests.get(url, headers=headers, timeout=5)

sleep(4)

soup = BeautifulSoup(result.text, 'lxml')
sleep(4)
data = soup.find('div', class_="product-card__price j-cataloger-price")
sleep(4)
print(data)