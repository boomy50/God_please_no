from async_generator import yield_
import requests
from bs4 import BeautifulSoup
import lxml
from time import sleep

# list_card_url = []

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
}

def downloads(url):
    resp = requests.get(url, stream=True)
    r = open(r'/home/yuriy/Рабочий стол/code/Parsing_WB_OZON/Pars/scrapingclub.com/image/' + url.split('/')[-1], 'wb')
    for value in resp.iter_content(1024*1024):
        r.write(value)
    r.close()


def get_url():
    for count in range (1, 2):
        sleep(1)
        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'
        response = requests.get(url, headers = headers)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find_all('div', class_ = "col-lg-4 col-md-6 mb-4")

        for i  in data:
            card_url ='https://scrapingclub.com' + i.find('a').get('href')
            yield card_url
            # list_card_url.append(card_url)
        
def array():
    for card_url in get_url():
        
        response = requests.get(card_url, headers = headers)
        sleep(3)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find('div', class_ = "card mt-4 my-4")
        name = data.find('h3', class_ = 'card-title').text.replace('/n', '')
        price = data.find('h4').text
        description = data.find('p', class_ = 'card-text').text
        img_url = 'https://scrapingclub.com' + data.find ('img', class_ = 'card-img-top img-fluid').get('src')
        yield name, price, img_url, description
        downloads(img_url)
