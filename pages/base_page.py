# pages/base_page.py
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
class BasePage:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.initiate_function()

    def initiate_function(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            return True

        except:
            print("ERROR : URL is incorrect/Network Error")
            return False


    def enter_text(self, element_id, text):
        self.driver.find_element(By.XPATH, element_id).send_keys(text)

    def extract_text(self, element_id):
        extract_message = self.driver.find_element(By.XPATH, element_id).text
        return extract_message

    def extract_employee_id(self, element_id):
        self.employee_id_detail = self.driver.find_element(By.XPATH, element_id).text
        print("Newly created employee id:", self.employee_id_detail)

    def click_element(self, element):
        self.driver.find_element(By.XPATH, element).click()

    def element_present(self, element_id):
        self.driver.find_element(By.XPATH, element_id)

    def select_radio_button(self, radio_button_xpath):
        radio_button = self.driver.find_element(By.XPATH, radio_button_xpath)
        if not radio_button.is_selected():
            radio_button.click()

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 750);")

    def handle_popup(self, delete_element):
        try:
            popup = self.driver.find_element(By.CLASS_NAME, "orangehrm-dialog-popup")
            yes_delete_button = popup.find_element(By.XPATH, delete_element)
            yes_delete_button.click()
        except:
            print("Popup not found or already closed.")

    def is_element_present(self, element_id):
        try:
            self.driver.find_element(By.XPATH, element_id)
            return True
        except:
            return False

    def shutdown(self):
        return self.driver.quit()

