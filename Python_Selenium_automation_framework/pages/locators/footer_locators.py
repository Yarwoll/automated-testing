from selenium.webdriver.common.by import By


class FooterLocators:
    """This class stores the locators found with the Xpath strategy for all footer elements."""
    _ukrainer_email_field_footer = (By.XPATH, "//input[@id='mce-EMAIL']")
    _ukrainer__footer = (By.XPATH, "(//input[@id='login__password'])")
    _ukrainer_subscribe_button_footer = (By.XPATH, "//input[@id='mc-embedded-subscribe']")
    _ukrainer_facebook_footer = (By.XPATH, "//a[@href='https://www.facebook.com/ukrainer.net']")
    _ukrainer_twitter_footer = (By.XPATH, "//a[@href='https://twitter.com/ukrainer']")
    _ukrainer_instagram_footer = (By.XPATH, "//a[@href='https://www.instagram.com/ukrainer_net']")
    _ukrainer_youtube_footer = (By.XPATH, "//a[@href='https://youtube.com/c/UkrainerNet']")
    _ukrainer_telegram_footer = (By.XPATH, "//a[@href='https://t.me/ukrainer_net']//*[name()='svg']")
    _ukrainer_donate_footer = (By.XPATH, "//a[@class='btn'][normalize-space()='Donate']")
    _ukrainer_recomend_location_footer = (By.XPATH, "//a[normalize-space()='Recommend location']")
    _ukrainer_share_music_footer = (By.XPATH, "//a[normalize-space()='Share music']")
    _ukrainer_join_team_footer = (By.XPATH, "//a[normalize-space()='Join the team']")
    _ukrainer_about_footer = (By.XPATH, "//a[normalize-space()='About Us']")
    _ukrainer_culture_fund_footer = (By.XPATH, "//a[@class='footer-logo']")
