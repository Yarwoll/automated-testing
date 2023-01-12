"""Module used as a location for Chrome webdriver as well for storing its options"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_driver(browsername='Chrome'):
    """Method for choosing Chrome driver and options for it."""
    optObj = webdriver.ChromeOptions()
    optObj.add_argument("--start-maximized")
    optObj.add_argument("--incognito")
    optObj.add_argument("--headless")
    optObj.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=optObj)
    return driver
