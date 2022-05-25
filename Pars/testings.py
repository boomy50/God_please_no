# Отправляет запросы на сервер и получает ответы
import lxml
import requests
from bs4 import BeautifulSoup
# тоже что url
link = 'https://www.wildberries.ru/catalog/15061503/detail.aspx?targetUrl=XS'

# отправляем запрос: (get получаем данные с страницы) (post передача данных "авторизации")
# указываем формат для "парса": text для текстового варианта , content для байтового(картинки, файлы) 
response = requests.get(link).text

#Создаем объект.В этом случае объектом является страница  которую мы парсим.Так же парсер который будем использовать"lxml"
soup = BeautifulSoup(response, 'html.parser')
block = soup.find(id  = 'infoBlockProductCard')
# price = block.find('div', id ='infoBlockProductCard')
print(block)