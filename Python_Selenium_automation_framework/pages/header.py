import logging as log

from selenium.common.exceptions import*

from pages.basepage import BasePage
from pages.locators.header_locators import HeaderLocators
from test.execution_utils.main_data import TestData


class Header(BasePage, HeaderLocators, TestData):
    """Class with methods for interaction with header elements."""

    def __init__(self, driver_item, timeout=15):
        """Method for the opening of the Ukrainer's main page."""
        log.info('Opening base url')
        self.driver = driver_item
        super().__init__(self.driver, timeout=timeout)
        self.base_url = TestData.MAIN_URL

    def header_presence(self, timeout=20):
        """Method for verifying that main header elements are present"""
        log.info('Looking for header elements:logo, topics, about info and search field')
        try:
            self._find_elem_wait(element=self._ukrainer_logo_header, timeout=timeout)
            self._find_elem_wait(element=self._ukrainer_topics_header, timeout=timeout)
            self._find_elem_wait(element=self._ukrainer_about_header, timeout=timeout)
            self._find_elem_wait(element=self._ukrainer_search_icon_header, timeout=timeout)
            log.info("Ukrainer's logo, topics, about info and search field from header are present")
            return True
        except NoSuchElementException as ex:
            log.warning('No header elements found, based on {}'.format(ex))
            return False

    def filling_search_field(self, search_input):
        """Method for filling data in header search field."""
        log.info('Inputting data for search request')
        self._find_element_click(input_locator=self._ukrainer_search_icon_header)
        self._type_into_input(input_locator=self._ukrainer_search_field_header, text=search_input)

    def submitting_search_request(self):
        """Method for filling data in search field."""
        self._press_enter_for_input(input_locator=self._ukrainer_search_field_header)

    def check_search_url(self, text):
        """Method for checking the presence of the search word in the page URL after submitting the search request."""
        try:
            current_window = self._get_current_window_url()
            if text in current_window:
                return True
        except NoSuchWindowException as ex:
            log.warning('No search text in the in the window url found, based on{}'.format(ex))
            log.info('Current search url is {}'.format(current_window))
            return False

    def check_search_title(self, timeout=20):
        """Method for checking the presence of the search word in the search title after submitting a search request."""
        try:
            self._get_element_text(element=self._ukrainer_search_result, text='expedition')
            return True
        except NoSuchElementException as ex:
            log.warning('No search text in the in the window title found, based on{}'.format(ex))
            return False

    def change_site_language(self):
        """Method for changing the site language to Ukrainian after opening the English version of the site."""
        self._find_element_click(input_locator=self._ukrainer_language_header)
        self._find_element_click(input_locator=self._ukrainer_ua_lang_header)

    def check_ua_element_text(self):
        """Method to assert presence of the elements in Ukrainian after changing language to UA."""
        log.info('Looking for elements with Ukrainian localization')
        try:
            self._get_element_text(element=self._ukrainer_war_ua_header, text='ВІЙНА')
            self._get_element_text(element=self._ukrainer_about_ua_header, text='ПРО UKRAЇNER')
            return True
        except NoSuchElementException as ex:
            log.warning('No Ukrainian localization found, based on{}'.format(ex))
            return False
