import requests
from bs4 import BeautifulSoup
import useragent


ua = useragent
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
}


def without_post(url, headers):
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		soup = BeautifulSoup(response.text, 'html.parser')
		links = {}
		for i in soup.find_all('a', {'class': 'post__title_link'}):
			links.update({i.text: i.get('href')})
		return links
	else:
		print("Connection Error")

url = "https://habr.com/ru/"
links = without_post(url, headers)
with open('parsed.txt', 'w') as f_obj:
	for name, href in links.items():
		f_obj.write(name + ':\n' + href + '\n\n')