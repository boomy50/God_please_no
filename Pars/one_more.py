from pyexpat import ParserCreate
from urllib import response
from lxml import etree
from bs4 import BeautifulSoup
import requests
import time


def parser():
    link = 'https://vk.com/login?u=2&to=/al_im.php?sel=c121'
    response = requests.get(link).text
    soup = BeautifulSoup(response, 'lxml')
    price_soup = soup.prettify()
    # block = soup.find(id = 'infoBlockProductCard')
    price_find = price_soup.find('div', id = 'infoBlockProductCard')
    
    return price_find

print(parser())

# def rang_cart():
