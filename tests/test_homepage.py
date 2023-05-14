from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest
from pages.Basepage import Homepage
from selenium import webdriver
from selenium.webdriver.common.by import By


class Assignment(unittest.TestCase):
    s = Service("/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # Validates sofas are available
    def test_sofas(self):
        homepage = Homepage(self.driver)  # Create an instance of the Homepage class
        homepage.test_valid_homepage()
        time.sleep(2)
        homepage.test_main_menu()
        time.sleep(3)
        homepage.test_products()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'ריהוט לבית')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'ספות')]").click()
        time.sleep(2)
        expected_url = 'https://www.ikea.com/il/he/cat/sofas-fu003/'
        current_url = self.driver.current_url
        self.assertEqual(current_url, expected_url, "URLs do not match")

    # Validates Chairs are available
    def test_chairs(self):
        homepage = Homepage(self.driver)
        homepage.test_valid_homepage()
        homepage.test_main_menu()
        time.sleep(3)
        homepage.test_products()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'ריהוט לבית')]").click()
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "כסאות").click()
        time.sleep(3)
        expected_url = 'https://www.ikea.com/il/he/cat/chairs-fu002/'
        current_url = self.driver.current_url
        self.assertEqual(current_url, expected_url, "URLs do not match")

    # Checks for desk
    def test_search_desk(self):
        homepage = Homepage(self.driver)
        homepage.test_valid_homepage()
        self.driver.find_element(By.CSS_SELECTOR, "#ikea-search-input").send_keys("שולחן כתיבה")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[@aria-label='שולחן כתיבה']").click()
        time.sleep(2)
        element_id = "//b[contains(text(),'שולחן כתיבה')]"
        element = self.driver.find_element(By.XPATH, element_id)
        self.assertTrue(element, f"Element with XPATH '{element_id}' is not present")

    # Checks for closet
    def test_search_closet(self):
        homepage = Homepage(self.driver)
        homepage.test_valid_homepage()
        self.driver.find_element(By.CSS_SELECTOR, "#ikea-search-input").send_keys("ארון בגדים")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[@aria-label='ארון בגדים']").click()
        time.sleep(2)
        elemento_id = "//b[contains(text(),'ארון בגדים')]"
        elemento = self.driver.find_element(By.XPATH, elemento_id)
        self.assertTrue(elemento, f"Element with XPATH '{elemento_id}' is not present")

    # Checks for bedroom
    def test_bedroom(self):
        homepage = Homepage(self.driver)
        homepage.test_valid_homepage()
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "חדרים")
        element_id_one = "//span[contains(text(),'חדרים')]"
        element_one = self.driver.find_element(By.XPATH, element_id_one)
        self.assertTrue(element_one, f"Element with XPATH '{element_id_one}' is not present")

    # Verifies you can view new products page
    def test_new_products(self):
        homepage = Homepage(self.driver)
        homepage.test_valid_homepage()
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "מוצרים חדשים").click()
        expected_url = 'https://www.ikea.com/il/he/new/'
        actual_url = self.driver.current_url
        self.assertEqual(actual_url, expected_url, "URLs do not match")

    # Verifies you can view your favorites
    def test_favorites(self):
        homepage = Homepage(self.driver)
        homepage.test_valid_homepage()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[@aria-label='רשימת קניות']//span[@class='hnf-btn__inner']").click()
        expected_url = 'https://www.ikea.com/il/he/'
        actual_url = self.driver.current_url
        self.assertEqual(actual_url, expected_url, "URLs do not match")

    # Verifies you can view youtube
    def test_youtube(self):
        homepage = Homepage(self.driver)
        homepage.test_valid_homepage()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[@aria-label='youtube']").click()
        expected_url = 'https://www.youtube.com/channel/UC2Pg3Uj9OGAfuOsKbyyo_Uw'
        actual_url = self.driver.current_url
        self.assertEqual(actual_url, expected_url, "URLs do not match")

    # Verifies you can view Facebook
    def test_facebook(self):
        homepage = Homepage(self.driver)
        homepage.test_valid_homepage()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[@aria-label='facebook']").click()
        expected_url = 'https://www.facebook.com/IKEAIL'
        actual_url = self.driver.current_url
        self.assertEqual(actual_url, expected_url, "URLs do not match")

    # Verifies you can view Instagram
    def test_instagram(self):
        homepage = Homepage(self.driver)
        homepage.test_valid_homepage()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[@aria-label='instagram']").click()
        expected_url = 'https://www.instagram.com/ikea_il/'
        actual_url = self.driver.current_url
        self.assertEqual(actual_url, expected_url, "URLs do not match")


if __name__ == "__main__":
    unittest.main()
