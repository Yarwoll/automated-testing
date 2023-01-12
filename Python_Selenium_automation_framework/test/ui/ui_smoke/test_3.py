from pages.footer import Footer


def test_header_search(driver_item):
    """Test for checking ability to go to the donation page after clicking on the footer's donate element."""
    search_process = Footer(driver_item)
    search_process._open_base_page()
    assert search_process.footer_presence()
    search_process.clicking_on_donate_option()
    assert search_process.checking_donate_url()
