from requests import session
from bs4 import BeautifulSoup
from time import sleep 
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
}

work = session()
work.get('https://quotes.toscrape.com/', headers = headers)
response = work.get('https://quotes.toscrape.com/login', headers = headers)
soup = BeautifulSoup(response.text, 'lxml')
token = soup.find('form').find('input').get('value')
data = {'csrf_token' : token, 'username' : 'noname', 'password' : 'password'}
result = work.post('https://quotes.toscrape.com/login', headers = headers, data = data, allow_redirects= True)
'https://quotes.toscrape.com/login'