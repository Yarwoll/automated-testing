from pages.header import Header
from test.execution_utils.main_data import TestData


def test_change_lang_header(driver_item):
    """Test for checking the ability to change language from English to Ukrainian with header language icon."""
    search_process = Header(driver_item)
    search_process._open_base_page()
    assert search_process.header_presence()
    search_process.change_site_language()
    assert search_process.check_search_url(text=TestData.MAIN_URL_UA)
    assert search_process.check_ua_element_text()
