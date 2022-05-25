from dis import dis, disco
import requests
from bs4 import BeautifulSoup
import pandas
from pandas import ExcelWriter
import openpyxl
import lxml

url = 'https://www.wildberries.ru/brands/xiaomi/all'
headers = {
    "Accept": "*/*",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
}


def get_html(url, params=None):
    response = requests.get(url, headers=headers, params=params)
 
    if url.status_code == 200:
        print('Все в норме!')
 
    if url.status_code == 404:
        print('Страница не существует!')

get_html()

def get_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        good_count = soup.find('span', class_='goods-count').get_text(strip=True).replace("\xa0", '').split()[0]
        print(good_count)
        pages = int(good_count)//100 + 1
    except:
        pages = 1

        return pages


def get_content(url):
    soup = BeautifulSoup.get(html, 'html.parser')
    items = soup.find_all('div', class_='product-card')
    cards = []

#  проверка на наличии скидки, если нет, то поле пустое
    for item in items:
        discount = item.find('span', class_='product-card__sale')
        try:
            if discount:
                discount = discount.get_text(strip=True)
            else:
                discount = item.find('span', class_ = 'product-card__sale').get_text(strip=True)
        except:
            discount = ''
 
        try:
            price=item.find(class_='lower-price').get_text(strip=True).replace('\xa0','').replace('₽', '')
        except:
            price = item.find('span', class_='price-commission__current-price').get_text(strip=True).replace('\xa0', '').replace('₽', '')
    
    cards.append({
            'brand': item.find('strong', class_='brand-name').get_text(strip=True).replace('/', ''),
            'title': item.find('span', class_='goods-name').get_text().split('/')[0],
            'price': int(item.find(class_='lower-price').get_text(strip=True).replace('\xa0', '').replace('₽', '')),
            'discount': discount,
            'link': f'https://www.wildberries.ru{item.find("a", class_="product-card__main").get("href")}',
        })
    return cards
        
def save_exel(data):
    # сохраняем полученные данные в эксель с помощью dataframe от pandas
    dataframe = pandas.DataFrame(data)
    newdataframe = dataframe.rename(columns={'brand': 'Брэнд', 'title': 'Наименование',
                                             'price': 'Цена',  'discount': 'Скидка',
                                             'link': 'Ссылка'})
    writer = ExcelWriter(f'data.xlsx')
    newdataframe.to_excel(writer, 'data')
    writer.save()
    print(f'Данные сохранены в файл "data.xlsx"')

