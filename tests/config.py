import os
from time import time

from selenium.webdriver.common.by import By

DOWNLOAD_PATH = os.path.join(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
), 'downloads')
FILE_NAME = 'sbisplugin-setup-web.exe'
FILE_PATH = os.path.join(DOWNLOAD_PATH, FILE_NAME)
URL = {
    'sbis': 'https://sbis.ru/',
    'tensor_about': 'https://tensor.ru/about',
}
ELEMENT = {
    'contact': (
        By.XPATH,
        '//ul[@class="sbisru-Header__menu ws-flexbox ws-align-items-center"]'
        '/descendant::a[text()="Контакты"]'
    ),
    'tensor_logo': (
        By.XPATH,
        '//a[@class="sbisru-Contacts__logo-tensor mb-12"]'
    ),
    'block_strength_in_people': (
        By.CSS_SELECTOR, ".tensor_ru-Index__block4-bg"
    ),
    'block_strength_in_people_more': (
        By.CSS_SELECTOR,
        'a.tensor_ru-link.tensor_ru-Index__link[href="/about"]'
    ),
    'photo': (
        By.XPATH,
        '//*[@class="s-Grid-col s-Grid-col--3 tensor_ru-About--col-md6 '
        'tensor_ru-About__block3--col-sm12"]/descendant::img'
    ),
    'region': (
        By.XPATH,
        '//span[@class="sbis_ru-Region-Chooser '
        'ml-16 ml-xm-0"]/descendant::span'
    ),
    'block_partners': (
        By.XPATH,
        '//div[@class="sbisru-Contacts-List__col '
        'ws-flex-shrink-1 ws-flex-grow-1"]'
    ),
    'kamchatka': (
        By.XPATH,
        '//*[@class="sbis_ru-Region-Panel__item"]'
        '/descendant::span[text()="41 Камчатский край"]'
    ),
    'region_partners': (
        By.XPATH,
        '//*[@id="city-id-2"]'
    ),
    'download_local': (
        By.XPATH,
        '//a[text()="Скачать локальные версии"]'
    ),
    'download': (
        By.XPATH,
        '//*[@class="sbis_ru-DownloadNew-loadLink__link js-link" '
        'and contains(text(), "Скачать (Exe")]'
    ),
}
ERRMSG = {
    'block': 'Блок отсутствует на странице',
    'endpoint': 'Ссылки не совпадают',
    'photo_size': 'Размеры фото не совпадают',
    'region': 'Регион определён неверно',
    'region_partners': 'Блок партнёров не обновился',
    'region_URL': 'Выбранный регион отсутсвует в URL',
    'region_title': 'Выбранный регион отсутсвует в title',
    'download': 'Файл не был скачан',
    'download_size': 'Размер скачанного файла не соответсвует'
}
INFOMSG = {
    'block': 'Блок присутствует на странице',
    'endpoint': 'Ссылки совпадают',
    'photo_size': 'Размеры фото совпадают',
    'region': 'Регион определён верно',
    'region_partners': 'Блок партнёров обновился',
    'region_URL': 'Выбранный регион присутствуе в URL',
    'region_title': 'Выбранный регион присутствуе в title',
    'download': 'Файл был скачан',
    'download_size': 'Размер скачанного файла соответсвует'
}


def time_and_chek(max_time):
    """
    Функция проверки наличия файла в указанный времменной период.
    """
    time_now = time()

    while time() - time_now <= max_time:
        if os.path.exists(FILE_PATH):
            return True
    return False
