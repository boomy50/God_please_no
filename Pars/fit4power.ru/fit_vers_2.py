import requests
from bs4 import BeautifulSoup
import lxml


headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
}

spisok = []

def get_url():
    
    url = 'https://fit4power.ru/programm'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all('div')
    
    for  i in data:
        prog_urls = 'https://fit4power.ru/programm' + i.find('a').get('href')
        spisok.append(prog_urls)
        print(spisok)

get_url()