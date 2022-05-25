from syslog import LOG_LPR
import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/?page=1'

lol = requests.get(url)

soup = BeautifulSoup(lol.text, 'lxml')

data = soup.find('div', class_ = 'card-body')

print(data)