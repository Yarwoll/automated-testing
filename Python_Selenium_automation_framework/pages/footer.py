import logging as log

from selenium.common.exceptions import*

from pages.basepage import BasePage
from pages.locators.footer_locators import FooterLocators
from test.execution_utils.main_data import TestData


class Footer(BasePage, FooterLocators, TestData):
    """Class with methods for interaction with footer  elements."""

    def __init__(self, driver_item, timeout=15):
        """Method for the opening of the Ukrainer's main page."""
        log.info('Opening base url')
        self.driver = driver_item
        super().__init__(self.driver, timeout=timeout)
        self.base_url = TestData.MAIN_URL

    def footer_presence(self, timeout=20):
        """Method for verifying that main footer elements are present"""
        log.info('Looking for footer elements: about, culture fund link, share music and join team options')
        try:
            log.info('Looking for footer elements: about, culture fund link, share music and join team options')
            self._find_elem_wait(element=self._ukrainer_about_footer, timeout=timeout)
            self._find_elem_wait(element=self._ukrainer_culture_fund_footer, timeout=timeout)
            self._find_elem_wait(element=self._ukrainer_share_music_footer, timeout=timeout)
            self._find_elem_wait(element=self._ukrainer_join_team_footer, timeout=timeout)
            log.info("Ukrainer's footer elements are present")
            return True
        except NoSuchElementException as ex:
            log.warning('No footer elements found, based on {}'.format(ex))
            return False

    def clicking_on_donate_option(self):
        """Method for clicking on the donate option from the footer."""
        log.info('Clicking on the donate element')
        self._find_element_click(input_locator=self._ukrainer_donate_footer)

    def checking_donate_url(self, text='donate'):
        """Method for checking the presence of the donate word in the page URL after pressing
        on the footer's donate option."""
        log.info('Checking presence of the donate Url')
        try:
            current_window = self._get_current_window_url()
            if text in current_window:
                return True
            log.info('Url for donating is present')
        except NoSuchWindowException as ex:
            log.warning('No donate text in the in the window url found, based on{}'.format(ex))
            log.info('Current url is {}'.format(current_window))
            return False

    def clicking_on_culture_fond(self):
        """Method for clicking on the culture fund link from the footer."""
        log.info('Clicking on the culture fund element')
        self._find_element_click(input_locator=self._ukrainer_culture_fund_footer)

    def checking_culture_fund_url(self, text=TestData.UA_CULTURE_FOND_URL):
        """Method for checking presence of the culture fund url after clicking on its footer element."""
        log.info('Checking presence of the donate Url')
        try:
            current_window = self._get_current_window_url()
            if text == current_window:
                return True
            log.info('Url of culture fund is present')
        except NoSuchWindowException as ex:
            log.warning('No culture fund window url found, based on{}'.format(ex))
            log.info('Current url is {}'.format(current_window))
            return False
