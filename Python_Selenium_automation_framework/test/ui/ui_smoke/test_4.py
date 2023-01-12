from pages.footer import Footer


def test_header_search(driver_item):
    """Test for checking the ability to go to the culture fund page after clicking on  its footer's element."""
    search_process = Footer(driver_item)
    search_process._open_base_page()
    assert search_process.footer_presence()
    search_process.clicking_on_culture_fond()
    assert search_process.checking_culture_fund_url()
