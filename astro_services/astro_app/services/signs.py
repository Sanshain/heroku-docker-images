import logging
import os
import socket
from sys import platform

from selenium import webdriver
from datetime import datetime

# import requests
# from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options

logger = logging.getLogger(__name__)

opts = Options()
opts.headless = True
URL_PATTERN = r'https://sotis-online.ru/?chr=dt:{}085232;cid:2417766;sx:m;name:New%20chart'

GLOBES = (
    'Венера'
)

MARK_SIGNS = {
    'E': 'Водолей',
    '<': 'Телец',
    'F': 'Рыбы',
    'D': 'Козерог',
    '=': 'Близнецы',
    'C': 'Стрелец',
    '>': 'Рак',
    '@': 'Дева',
    'B': 'Скорпион',
    'A': 'Весы',
    ';': 'Овен',
}

def get_browser(log_path):    

    if platform.startswith('win') or True:        

        # works only to alpine | windows

        return webdriver.Firefox(
            executable_path=os.path.join(os.getcwd(), 'geckodriver'),
            options=opts,
            service_log_path=log_path
        )
    else:

        # works only for ubuntu | mint

        browser = webdriver.PhantomJS(
            # executable_path=os.path.join(os.getcwd(), 'phantomjs'),
            executable_path=os.path.join(os.getcwd(), 'phantom_js', 'bin', 'phantomjs'),
            port=8081,
            service_log_path=log_path,
            service_args=[
                '--debug=true', 
                # '--ssl-protocol=tlsv1.2', 
                '--ignore-ssl-errors=true'
            ]
        )
        browser.set_window_size(800, 600)
        return browser


def get_sign(date=None, base='Венера'):
    """
    парсит значение знака для планеты
    :param date:
    :param base:
    :return:
    """
    if base not in GLOBES: raise Exception('Invalid base globe name')
    date = date or datetime.today()

    log_path = os.path.join(os.getcwd(), '.logs', 'gecko_driver.log')

    browser = get_browser(log_path)
    browser.get(URL_PATTERN.format(date.strftime('%Y%m%d')))

    # tag = browser.find_element_by_css_selector('th[data-t^="Венера"]')
    sign_mark = browser.execute_script(
        'return document.querySelector(\'th[data-t^="Венера"]\').nextElementSibling.nextElementSibling.innerText'
    )
    logger.info(sign_mark)

    browser.close()
    return MARK_SIGNS.get(sign_mark)


if __name__ == '__main__':
    print(get_sign())

# def _get_sign(date=None):
#     date = date or datetime.today()
#     page = requests.get(URL_PATTERN.format(date))
#     # data-t="Венера"
#     soup = BeautifulSoup(page.text, 'lxml')
#     selector = soup.find('th[data-t^="Венера"]')
#     return selector

# print(_get_sign(datetime.now()))
