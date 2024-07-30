import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators
        self.select_product_1 = "//*[@id='add-to-cart-sauce-labs-backpack']"
        self.select_product_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
        self.select_product_3 = "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
        self.cart = "//*[@id='shopping_cart_container']/a"
        self.menu = "//button[ @ id = 'react-burger-menu-btn']"
        self.about = "//a[@id='about_sidebar_link']"


    # Getters
    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))
    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))
    def get_select_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_about(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.about)))



    # Actions
    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("select product 1")

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("select product 2")

    def click_select_product_3(self):
        self.get_select_product_3().click()
        print("select product 3")
    def click_cart(self):
        self.get_cart().click()
        print("clicl cart")

    def click_menu(self):
        self.get_menu().click()
        print("click menu")

    def click_about(self):
        self.get_about().click()
        print("click about")


    # Methods

    def select_menu_about(self):
        with allure.step("Select menu about"):
            Logger.add_start_step(method="select_menu_about")
            self.get_current_url()
            self.click_menu()
            self.click_about()
            Logger.add_end_step(url=self.driver.current_url, method="select_menu_about")

    def select_products_1(self):
        with allure.step("Select products 1"):
            Logger.add_start_step(method="select_products_1")
            self.get_current_url()
            self.click_select_product_1()
            self.click_cart()
            # self.assser_url("https://saucelabs.com/")
            Logger.add_end_step(url=self.driver.current_url, method="select_products_1")
            time.sleep(3)

    def select_products_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()
        time.sleep(3)

    def select_products_3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()
        time.sleep(3)