from pages.pages import TestHelper
from tests import config


def test_first_route(browser):
    main_page = TestHelper(browser, config.URL['sbis'])
    main_page.go_to_site()

    main_page.go_to_PATH(config.ELEMENT['contact'])
    main_page.go_to_PATH(config.ELEMENT['tensor_logo'])

    main_page.switch_tab(1)
    assert main_page.check_exist_element(
        config.ELEMENT['block_strength_in_people']), 'Блок отсутствует'

    main_page.go_to_PATH(config.ELEMENT['block_strength_in_people_more'])
    assert browser.current_url == config.URL['tensor_about'], 'Ссылки не совпадают'

    photo_size = main_page.get_photo_size(config.ELEMENT['photo'])
    for count, data in enumerate(photo_size):
        if count == len(data) - 1:
            break
        assert data == photo_size[count+1]
