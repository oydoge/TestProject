import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Login_page(Base):
    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators
        self.user_name = "//input[@id='user-name']"
        self.password = "//input[@id='password']"
        self.login_button = "//input[@id='login-button']"
        self.main_word = "//span[@class='title']"

    # Getters
    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions
    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("input user name good")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("input password good")

    def click_login_button(self):
        self.get_login_button().click()
        print("input login button click")

    # Methods
    def autorization(self):
        with allure.step("autorization"):
            Logger.add_start_step(method="autorization")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_user_name("standard_user")
            self.input_password("secret_sauce")
            self.click_login_button()
            self.assert_word(self.get_main_word(), 'Products')
            Logger.add_end_step(url=self.driver.current_url, method="autorization")
            time.sleep(3)