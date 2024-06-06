# tests/test_home_page.py
import pytest
from pages.home_page import HomePage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium import webdriver

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
file_path = "C:\\workspace\\Capstone_Project02_orangeHR\\resources\\login_details.xlsx"
sheet_name = "login"


base_page = BasePage(url)
login_page = LoginPage(base_page.driver)
home_page = HomePage(base_page.driver)


@pytest.mark.order(1)
def test_TC_PIM_03_menu_validation():
    login_page.login_user(file_path, sheet_name)
    home_page.validate_menu_options()

@pytest.mark.order(2)
def test_TC_PIM_02_header_validation():
    home_page.validate_headers()


@pytest.mark.order(3)
def test_shutdown():
    home_page.shutdown()
