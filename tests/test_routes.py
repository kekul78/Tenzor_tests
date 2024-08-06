import os

from pages.pages import TestHelper
from tests.config import URL, ELEMENT, ERRMSG, FILE_PATH, time_and_chek


def test_first_route(browser):
    main_page = TestHelper(browser, URL['sbis'])
    main_page.go_to_site()

    main_page.go_to_PATH(ELEMENT['contact'])
    main_page.go_to_PATH(ELEMENT['tensor_logo'])

    main_page.switch_tab(1)
    assert main_page.check_exist_element(
        ELEMENT['block_strength_in_people']), ERRMSG['block']

    main_page.go_to_PATH(ELEMENT['block_strength_in_people_more'])
    assert (
        browser.current_url == URL['tensor_about']
    ), ERRMSG['endpoint']

    photo_size = main_page.get_photo_size(ELEMENT['photo'])
    for count, data in enumerate(photo_size):
        if count == len(data) - 1:
            break
        assert data == photo_size[count+1]


def test_second_route(browser):
    main_page = TestHelper(browser, URL['sbis'])
    main_page.go_to_site()

    main_page.go_to_PATH(ELEMENT['contact'])
    assert (
        main_page.find_ellement_with_text(ELEMENT['region'],
                                          'Ярославская обл.')
        ), ERRMSG['region']

    assert main_page.check_exist_element(
        ELEMENT['block_partners']), ERRMSG['block']

    main_page.go_to_PATH(ELEMENT['region'])
    main_page.go_to_PATH(ELEMENT['kamchatka'])
    assert (
        main_page.find_ellement_with_text(ELEMENT['region'],
                                          'Камчатский край')
        ), ERRMSG['region']

    assert (
        main_page.find_ellement_with_text(ELEMENT['region_partners'],
                                          'Петропавловск-Камчатский')
        ), ERRMSG['region_partners']

    assert (
        '41-kamchatskij-kraj' in browser.current_url
    ), ERRMSG['region_URL']

    assert (
        'СБИС Контакты — Камчатский край' in browser.title
    ), ERRMSG['region_title']


def test_third_route(browser):
    main_page = TestHelper(browser, URL['sbis'])
    main_page.go_to_site()

    main_page.go_to_PATH(ELEMENT['download_local'])

    main_page.go_to_PATH(ELEMENT['download'])
    assert time_and_chek(20), ERRMSG['download']

    file_text = main_page.find_element(ELEMENT['download']).text
    file_size = float(file_text.split()[2])
    downlad_file_size = round((os.path.getsize(FILE_PATH) / 1024**2), 2)

    assert file_size == downlad_file_size

    os.remove(FILE_PATH)
