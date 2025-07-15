import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestGoogleDoodles(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_doodles_redirect(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        time.sleep(2)

        try:
            agree_button = driver.find_element(By.XPATH, "//button[contains(., 'Aceitar')]")
            agree_button.click()
            time.sleep(1)
        except:
            pass  

      lucky_button = driver.find_element(By.NAME, "btnI")
        lucky_button.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
