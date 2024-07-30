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

# @pytest.mark.run(order=3)
@allure.description("Test buy product 1")
def test_buy_product_1():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    print("START TEST 1")

    login = Login_page(driver)
    login.autorization()

    mp = Main_page(driver)
    mp.select_products_1()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    cip = Client_information_page(driver)
    cip.uinput_information()

    pg = Payment_page(driver)
    pg.payment()

    fg = Finish_page(driver)
    fg.finish()

#python -m pytest -s -v
    print("FINISH TEST")
    time.sleep(10)
    driver.quit()


# @pytest.mark.run(order=1)
# def test_buy_product_2():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
#     print("START TEST 2")
#
#     login = Login_page(driver)
#     login.autorization()
#
#     mp = Main_page(driver)
#     mp.select_products_2()
#
#     cp = Cart_page(driver)
#     cp.click_checkout_button()
#
# #python -m pytest -s -v
#     print("FINISH TEST")
#     time.sleep(10)
#     driver.quit()
# @pytest.mark.run(order=2)
# def test_buy_product_3():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
#     print("START TEST 3")
#
#     login = Login_page(driver)
#     login.autorization()
#
#     mp = Main_page(driver)
#     mp.select_products_3()
#
#     cp = Cart_page(driver)
#     cp.click_checkout_button()
#
#
#
# #python -m pytest -s -v test_buy_product.py
#     print("FINISH TEST")
#     time.sleep(10)
#     driver.quit()

# pip install selenium
# pip install webdriver-manager
# pip install pytest
# pip install pytest-order
# python -m pytest --alluredir=test_results/ tests/test_buy_product.py

# cd C:\Users\Vladimir\PycharmTests\"name of project">allure serve test_results/
# allure serve test_results/


