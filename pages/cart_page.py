import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators
        self.checkout_button = "//button[@class='btn btn_action btn_medium checkout_button ']"



    # Getters
    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))


    # Actions
    def click_checkout(self):
        self.get_checkout_button().click()
        print("click chekout button ")


    # Methods
    def click_checkout_button(self):
        with allure.step("Click checkout button"):
            Logger.add_start_step(method="click_checkout_button")
            self.get_current_url()
            self.click_checkout()
            Logger.add_end_step(url=self.driver.current_url, method="click_checkout_button")
            time.sleep(3)
