from pages.login_page import LoginPage
from pages.base_page import BasePage

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

base_page = BasePage(url)
login_page = LoginPage(base_page.driver)


def test_TC_PIM_01_reset_password():
    reset_user = {
        'user': "DEMO"
    }
    login_page.reset_password(reset_user)


def test_shutdown():
    login_page.shutdown()
