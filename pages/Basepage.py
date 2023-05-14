from selenium import webdriver
from selenium.webdriver.common.by import By


class Homepage():
    def __init__(self, driver):
        self.driver = driver

    def test_valid_homepage(self):
        self.driver.get("https://www.ikea.com/il/he/")

    def test_main_menu(self):
        self.driver.find_element(By.XPATH, "//div[@class='hnf-header-hamburger hnf-page-container']//div[@class='hnf-page-container__aside']").click()

    def test_products(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[data-tracking-label='products']").click()
