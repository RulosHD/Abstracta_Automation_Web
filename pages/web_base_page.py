from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class web_base_page:

    def __init__(self, driver):
        self.driver = driver
    
    def find_element_by_xpath(self, xpath):
        return self.driver(f"return {js_query}")

    def is_displayed(self, element, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of(element))
            return True
        except NoSuchElementException or StaleElementReferenceException as ex:
            print("Exception al elemento {element}: "+str(ex))    
            return False
    
    def is_enabled(self, element, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(element))
            return True
        except NoSuchElementException or StaleElementReferenceException as ex:
            print("Exception al elemento {element}: "+str(ex))
            return False

    def wait_until_element_is_visible(self, xpath):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException as ex:
            print("No se encuentra el elemento despues de 30 segundos: " + str(ex))

    
    def wait_until_element_is_clickeable(self, xpath):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutException as ex:
            print("No se encuentra el elemento despues de 30 segundos: " + str(ex))
    
    