from selenium.webdriver.common.by import By


class HeaderLocators:
    """This class stores the locators found with the Xpath(mainly) strategy for all header elements.
    Part 'ua' in the locator name tells that element is a part of the Ukrainian language localization"""
    _ukrainer_logo_header = (By.XPATH, "//a[@class='logo']//*[name()='svg']")
    _ukrainer_war_ua_header = (By.XPATH, "//a[@class='main-link war-ua']")
    _ukrainer_regions_header = (By.XPATH, "//a[normalize-space()='Regions']")
    _ukrainer_topics_header = (By.XPATH, "//a[@class='main-link'][normalize-space()='Topics']")
    _ukrainer_about_header = (By.XPATH, "//a[normalize-space()='About']")
    _ukrainer_about_ua_header = (By.XPATH, "//a[contains(text(),'Про Ukraїner')]")
    _ukrainer_shop_header = (By.XPATH, "//a[normalize-space()='Shop']")
    _ukrainer_donate_header = (By.XPATH, "//a[@class='main-link'][normalize-space()='Donate']")
    _ukrainer_movie_header = (By.XPATH, "//a[normalize-space()='The Movie']")
    _ukrainer_language_header = (By.XPATH, "//i[@class='zmdi zmdi-caret-down']")
    _ukrainer_eng_lang_header = (By.XPATH, "//a[normalize-space()='(EN) English']")
    _ukrainer_ua_lang_header = (By.CSS_SELECTOR, "header[class='container lang-list-opened'] li:nth-child(1)")
    _ukrainer_search_icon_header = (By.XPATH, "(//i[@class='zmdi zmdi-search'])[1]")
    _ukrainer_search_field_header = (By.XPATH, "//input[@id='s']")
    _ukrainer_search_result = (By.XPATH, "//h1[@class='search-resault__title']")
