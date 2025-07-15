import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestHerokuAppLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_login_success(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/login")

        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")
        username_input.send_keys("tomsmith")
        password_input.send_keys("SuperSecretPassword!")

        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        time.sleep(2)

        success_message = driver.find_element(By.ID, "flash").text
        self.assertIn("You logged into a secure area!", success_message)

    def test_login_failure(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/login")

        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")
        username_input.send_keys("wronguser")
        password_input.send_keys("wrongpassword")

        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        time.sleep(2)

        error_message = driver.find_element(By.ID, "flash").text
        self.assertIn("Your username is invalid!", error_message)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
