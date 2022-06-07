import requests
from bs4 import BeautifulSoup
import lxml

list_text_url = []

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
}
def get_url():
    for n in range(1, 3):
        url = 'https://fit4power.ru/programm'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find('div', id = 'middle-column')
        for i in data:
            text_url = 'https://fit4power.ru' + data.find('a').get('href')           
            yield text_url # list_text_url.append(text_url)

def find_traning():
    for text_url in get_url():
        response = requests.get(text_url, headers = headers)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find('div', id = 'middle-column')
        all_text = soup.find('div', id = 'articlewrap').text
        # name_traning = data.find('span', style = 'font-family: georgia, palatino;')
        # text_trane = data.find('p', style = 'text-align: justify;').text

