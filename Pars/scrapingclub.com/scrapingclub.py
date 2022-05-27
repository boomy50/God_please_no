import requests
from bs4 import BeautifulSoup
import lxml
from time import sleep

list_card_url = []

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
}

for count in range (1, 2):
    sleep(1)
    url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'
    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all('div', class_ = "col-lg-4 col-md-6 mb-4")

    # for i in data:
    #     name = i.find('h4', class_= 'card-title').text.replace('/', '')
    #     price = i.find('h5').text
    #     url_img = 'https://scrapingclub.com' + i.find('img', class_ = "card-img-top img-fluid").get('src')
    #     print(name + '\n' + price + '\n' + url_img + '\n\n')

    for i  in data:
        card_url ='https://scrapingclub.com' + i.find('a').get('href')
        list_card_url.append(card_url)
        

for card_url in list_card_url:
    response = requests.get(card_url, headers = headers)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('div', class_ = "card mt-4 my-4")
    name = data.find('h3', class_ = 'card-title').text.replace('/n', '')
    price = data.find('h4').text
    description = data.find('p', class_ = 'card-text').text
    img_url = 'https://scrapingclub.com' + data.find ('img', class_ = 'card-img-top img-fluid').get('src')