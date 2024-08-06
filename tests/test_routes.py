import os
import logging

from pages.pages import TestHelper
from tests.config import (
    URL, ELEMENT, ERRMSG, INFOMSG, FILE_PATH, time_and_chek
)

LOGGER = logging.getLogger(__name__)


def test_first_route(browser):
    """
    Проверка работы первого сценария
    переход по ссылкам, нажатие кнопок,
    проверка наличия блоков, проверка соответсвий размеров фотографий.
    """
    main_page = TestHelper(browser, URL['sbis'])
    main_page.go_to_site()

    main_page.go_to_PATH(ELEMENT['contact'])
    main_page.go_to_PATH(ELEMENT['tensor_logo'])

    main_page.switch_tab(1)
    assert main_page.check_exist_element(
        ELEMENT['block_strength_in_people']), LOGGER.error(ERRMSG['block'])
    LOGGER.info(INFOMSG['block'])

    main_page.go_to_PATH(ELEMENT['block_strength_in_people_more'])
    assert (
        browser.current_url == URL['tensor_about']
    ), LOGGER.error(ERRMSG['endpoint'])
    LOGGER.info(INFOMSG['endpoint'])

    photo_size = main_page.get_photo_size(ELEMENT['photo'])
    for count, data in enumerate(photo_size):
        if count == len(data) - 1:
            break
        assert data == photo_size[count+1], LOGGER.error(ERRMSG['photo_size'])
        LOGGER.info(INFOMSG['photo_size'])


def test_second_route(browser):
    """
    Проверка работы второго сценария
    переход по ссылкам, определение региона,
    проверка наличия блоков, проверка наличия текста в элементах.
    """
    main_page = TestHelper(browser, URL['sbis'])
    main_page.go_to_site()

    main_page.go_to_PATH(ELEMENT['contact'])
    assert (
        main_page.find_ellement_with_text(ELEMENT['region'],
                                          'Ярославская обл.')
        ), LOGGER.error(ERRMSG['region'])
    LOGGER.info(INFOMSG['region'])

    assert main_page.check_exist_element(
        ELEMENT['block_partners']), LOGGER.error(ERRMSG['block'])
    LOGGER.info(INFOMSG['block'])

    main_page.go_to_PATH(ELEMENT['region'])
    main_page.go_to_PATH(ELEMENT['kamchatka'])
    assert (
        main_page.find_ellement_with_text(ELEMENT['region'],
                                          'Камчатский край')
        ), LOGGER.error(ERRMSG['region'])
    LOGGER.info(INFOMSG['region'])

    assert (
        main_page.find_ellement_with_text(ELEMENT['region_partners'],
                                          'Петропавловск-Камчатский')
        ), LOGGER.error(ERRMSG['region_partners'])
    LOGGER.info(INFOMSG['region_partners'])

    assert (
        '41-kamchatskij-kraj' in browser.current_url
    ), LOGGER.error(ERRMSG['region_URL'])
    LOGGER.info(INFOMSG['region_URL'])

    assert (
        'СБИС Контакты — Камчатский край' in browser.title
    ), LOGGER.error(ERRMSG['region_title'])
    LOGGER.info(INFOMSG['region_title'])


def test_third_route(browser):
    """
    Проверка работы третьего сценария
    """
    main_page = TestHelper(browser, URL['sbis'])
    main_page.go_to_site()

    main_page.go_to_PATH(ELEMENT['download_local'])

    main_page.go_to_PATH(ELEMENT['download'])
    assert time_and_chek(20), LOGGER.error(ERRMSG['download'])
    LOGGER.info(INFOMSG['download'])

    file_text = main_page.find_element(ELEMENT['download']).text
    file_size = float(file_text.split()[2])
    downlad_file_size = round((os.path.getsize(FILE_PATH) / 1024**2), 2)

    assert (
        file_size == downlad_file_size
            ), LOGGER.error(ERRMSG['download_size'])
    LOGGER.info(INFOMSG['download_size'])

    os.remove(FILE_PATH)
