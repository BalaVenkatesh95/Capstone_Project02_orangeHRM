import time

from pages.base_page import BasePage
from utils.excel_util import read_excel, write_excel
from utils.helpers import element_clickable
from utils.helpers import wait_for_element
from utils.helpers import wait_for_element_presence
from utils.screenshot import take_screenshot
from selenium.webdriver.common.by import By
from utils.helpers import wait_for_alert


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def read_test_data(self, file_path, sheet_name):

        return read_excel(file_path, sheet_name)

    def write_test_results(self, file_path, sheet_name, data):

        write_excel(file_path, sheet_name, data)

    def login_user(self, file_path, sheet_name):
        self.username_field = "//input[@name='username' and @placeholder='Username']"
        self.password_field = "//input[@name='password' and @placeholder='Password']"
        self.login_button = "//button[@type='submit' and normalize-space()='Login']"
        self.profile_image_in_home_page = "//img[@class='oxd-userdropdown-img' and @alt='profile picture']"
        self.logout_button = "//a[@class='oxd-userdropdown-link' and normalize-space()='Logout']"
        self.invalid_message = "//p[text()='Invalid credentials']"

        # Read test data from Excel file
        test_data = self.read_test_data(file_path, sheet_name)

        # Iterate over each row of test data
        for row in test_data[1:]:  # Skip header row
            # Extract values from the current row based on column headers
            test_id = row[test_data[0].index("Test ID")]
            username = row[test_data[0].index("Username")]
            password = row[test_data[0].index("Password")]
            name_of_tester = row[test_data[0].index("Name of Tester")]

            wait_for_element(self.driver, self.username_field)
            self.enter_text(self.username_field, username)

            wait_for_element(self.driver, self.password_field)
            self.enter_text(self.password_field, password)

            element_clickable(self.driver, self.login_button)
            self.click_element(self.login_button)
            take_screenshot(self.driver)
            # alert = wait_for_alert(self.driver)
            # alert.accept()

            try:
                wait_for_element_presence(self.driver, self.profile_image_in_home_page)
                test_result = "Pass"
                row.append(test_result)
                # self.click_element(self.profile_image_in_home_page)
                # self.click_element(self.logout_button)
            except:
                test_result = "Fail"
                row.append(test_result)
                wait_for_element_presence(self.driver, self.invalid_message)
                self.extract_text(self.invalid_message)

        # Write updated test data (including test results) back to Excel file
        self.write_test_results(file_path, sheet_name, test_data)




    def reset_password(self, reset_user):
        self.username_field = "//input[@name='username' and @placeholder='Username']"
        self.forget_password_link = "//div[@class='orangehrm-login-forgot']//p[contains(normalize-space(.), 'Forgot your password?')]"
        self.reset_password_button = "//button[@type='submit' and normalize-space()='Reset Password']"
        self.reset_message = "//h6[contains(@class, 'orangehrm-forgot-password-title') and normalize-space(.) = 'Reset Password link sent successfully']"


        wait_for_element(self.driver, self.username_field)
        self.enter_text(self.username_field, reset_user['user'])

        element_clickable(self.driver, self.forget_password_link)
        self.click_element(self.forget_password_link)

        wait_for_element(self.driver, self.username_field)
        self.enter_text(self.username_field, reset_user['user'])
        element_clickable(self.driver, self.reset_password_button)
        self.click_element(self.reset_password_button)

        wait_for_element_presence(self.driver, self.reset_message)




