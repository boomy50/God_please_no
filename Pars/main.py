import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


def get_source_html(url):

    driver = webdriver.Firefox(
        executable_path='/home/yuriy/Рабочий стол/code/Parsing_WB_OZON/Pars/geckodriver/geckodriver'
    )
    driver.maximize_window()

    try:
        driver.get(url=url)
        time.sleep(7)
    
        while True:
            find_more_element = driver.find_element_by_class_name

    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()


def main():
    get_source_html(url='https://www.wildberries.ru/catalog/35109600/detail.aspx?targetUrl=SP')

if __name__ == '__main__':
    main()
    