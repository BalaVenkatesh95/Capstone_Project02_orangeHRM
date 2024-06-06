# pages/home_page.py


from pages.base_page import BasePage
from pages.login_page import LoginPage
from utils.helpers import element_clickable, wait_for_element_presence


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)


    def validate_headers(self):

        self.required_headers = [
            "//span[normalize-space(text())='User Management']",
            "//span[normalize-space(text())='Job']",
            "//span[normalize-space(text())='Organization']",
            "//span[normalize-space(text())='Qualifications']",
            "//a[text()='Nationalities']",
            "//a[text()='Corporate Branding']",
            "//span[normalize-space(text())='Configuration']"
        ]

        self.admin_button = "//aside//nav//ul[@class='oxd-main-menu']//a[contains(@href, 'viewAdminModule')]"
        self.left_slide_button = "//i[contains(@class, 'oxd-icon') and contains(@class, 'bi-chevron-left')]"
        wait_for_element_presence(self.driver, self.admin_button)
        element_clickable(self.driver, self.admin_button)
        self.click_element(self.admin_button)
        wait_for_element_presence(self.driver, self.left_slide_button)
        element_clickable(self.driver, self.left_slide_button)
        self.click_element(self.left_slide_button)

        missing_headers = []
        for header_xpath in self.required_headers:
            if not self.is_element_present(header_xpath):
                missing_headers.append(header_xpath)

        if not missing_headers:
            return True
        else:
            print(f"Missing headers: {missing_headers}")
            return False

    def validate_menu_options(self):
        self.required_menu_options = [
            "//span[text()='Admin']",
            "//aside[@class='oxd-sidepanel']//a[@class='oxd-main-menu-item']//span[text()='PIM']",
            "//span[text()='Leave']",
            "//span[text()='Time']",
            "//span[text()='Recruitment']",
            "//span[text()='My Info']",
            "//span[text()='Performance']",
            "//span[text()='Dashboard']",
            "//span[text()='Directory']",
            "//span[text()='Maintenance']",
            "//span[text()='Buzz']"
        ]

        missing_menu_options = []
        for menu_option_xpath in self.required_menu_options:
            if not self.is_element_present(menu_option_xpath):
                missing_menu_options.append(menu_option_xpath)

        if not missing_menu_options:
            return True
        else:
            print(f"Missing menu options: {missing_menu_options}")
            return False

