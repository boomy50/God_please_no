from syslog import LOG_LPR
from urllib import response
import requests
from bs4 import BeautifulSoup

# url = 'https://www.wildberries.ru/catalog/72207521/detail.aspx?targetUrl=XS'

response = requests.get('https://www.ozon.ru/category/knigi-16500/?category_was_predicted=true&from_global=true&text=%D0%BC%D0%B0%D1%80%D0%BA%D1%81')

soup = BeautifulSoup(response.text, 'lxml')

data = soup.find('div', class_ = 'i3u')

print(data.text)