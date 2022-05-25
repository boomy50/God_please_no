import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import lxml
import time



#####Получение статус кода и создание словаря с заголовками#####
url = 'https://www.wildberries.ru/catalog/35109600/detail.aspx?targetUrl=SP'

headers = {
    "Accept": "*/*",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
}

response = requests.get(url, headers=headers)
print(response.status_code)

###htmlстраницы###
html = response.text

#####Функция получения кода страницы#####
def get_html(url, params=None):
    response = requests.get(url, headers=headers, params=params)
    html = response.text
    return html
    
#####Функция получения числа страниц#####
def get_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        good_count = soup.find('span', class_='goods-count').get_text(strip=True).replace("\xa0", '').split()[0]
        print(good_count)
        pages = int(good_count) // 100 + 1
    except:
        pages = 1
    return pages

# print(get_pages(url))

#####Функция сбора данных get_content#####
def get_content():
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_="product-card")
    cards = []
    
    for item in items:
# проверка на наличии скидки, если нет, то поле пустое
        try:
            price=item.find(class_='lower-price').get_text(strip=True).replace('\xa0','').replace('₽', '')
        except:
            price = item.find('span', class_='price-commission__current-price').get_text(strip=True).replace('\xa0', '').replace('₽', '')
        
        try:
            discount = item.find('span', class_='product-card__sale active')
            if discount:
                discount = discount.get_text(strip=True)
            else:
                discount = item.find('span', class_='product-card__sale').get_text(strip=True)
        except:
            discount = ''