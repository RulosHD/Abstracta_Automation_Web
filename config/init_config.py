from config.browser_handler import browser_handler
from pages.opencart_page import opencart_page


def init_config(context):
    driver = browser_handler["chrome"]()
    context.driver = driver
    context.opencart_page = opencart_page(driver)