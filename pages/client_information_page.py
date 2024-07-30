import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

from base.base_class import Base
from utilities.logger import Logger

# Fake information
faker = Faker("en_US")
first_name_faker = faker.name()
last_name_faker = faker.last_name()
zip_code_faker = faker.zipcode()

class Client_information_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver




        # Locators
        self.first_name = "//input[@id='first-name']"
        self.last_name = "//input[@id='last-name']"
        self.zip_code = "//input[@id='postal-code']"
        self.continue_button = "//input[@id='continue']"


    # Getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_zip_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.zip_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    # Actions
    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("input user name good")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("input password good")

    def input_zip_code(self,zip_code):
        self.get_zip_code().send_keys(zip_code)
        print("input login button click")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("input login button click")



    # Methods
    def uinput_information(self):
        with allure.step("Uinput_information"):
            Logger.add_start_step(method="Input information")
            self.get_current_url()
            self.input_first_name(first_name_faker)
            self.input_last_name(last_name_faker)
            self.input_zip_code(zip_code_faker)
            time.sleep(3)
            self.click_continue_button()
            Logger.add_end_step(url=self.driver.current_url, method="uinput_information")
            time.sleep(3)