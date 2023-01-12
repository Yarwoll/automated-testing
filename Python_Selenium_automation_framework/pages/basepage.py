from pypom import Page

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as ec, expected_conditions


class BasePage(Page):
    """This class is the parent class for all the pages in application.
    The BasePage class holds all common functionality across the website."""

    def __init__(self, driver, timeout=60):
        """Function that is called every time a new object of the base class is created."""
        self.driver = driver
        self.timeout = timeout
        super().__init__(driver, timeout=timeout)

    def _open_base_page(self):
        """Method for opening main URL of the site ."""
        self.driver.get(self.base_url)

    def _find_elem_wait(self, element, timeout=30):
        """Method for waiting until an element is present in Selenium webdriver."""
        WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(element),
                                                  message='element is not availiable')
        return self.find_element(*element)

    def _find_element_click(self, input_locator):
        """Method for finding element and clicking on it."""
        element = self._find_elem_wait(element=input_locator)
        element.click()
        return element

    def _type_into_input(self, input_locator, text):
        """Method for finding element, clicking on it and sending keys(values)."""
        element = self._find_elem_wait(input_locator)
        element.send_keys(text)

    def _press_enter_for_input(self, input_locator):
        """Method for finding input element and pressing enter to submit input value ."""
        input_field = self._find_element_click(input_locator)
        input_field.send_keys(Keys.ENTER)

    def _get_current_window_url(self):
        """Method for finding the URL of the current window."""
        window_url = self.driver.current_url
        return window_url

    def _get_element_text(self, element, text):
        """Method created to get a text from the particular element for next checking"""
        element = self._find_elem_wait(element)
        element_text = element.text
        assert text in element_text
