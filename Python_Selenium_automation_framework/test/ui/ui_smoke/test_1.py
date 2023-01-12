from pages.header import Header


def test_header_search(driver_item):
    """Test for checking search ability with the header search field."""
    search_process = Header(driver_item)
    search_process._open_base_page()
    assert search_process.header_presence()
    search_process.filling_search_field(search_input='expedition')
    search_process.submitting_search_request()
    assert search_process.check_search_url(text='expedition')
    assert search_process.check_search_title()
