import time

import allure
import pytest
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page

from pages.payment_page import Payment_page


@allure.description("Test link about")
def test_link_about():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    print("START TEST 2")

    login = Login_page(driver)
    login.autorization()

    mp = Main_page(driver)
    mp.select_menu_about()

    print("Finish test 2")
    time.sleep(10)
    driver.quit()

#
#
# #python -m pytest -s -v test_link_about.py
# # cd C:\Users\Zver\PycharmProjects\PythonSelenium\main_project\tests