# utils/helpers.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def wait_for_element(driver, element_id, timeout=30):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.XPATH, element_id))
    )

def element_clickable(driver, element_id, timeout=30):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.XPATH, element_id))
    )

def wait_for_element_presence(driver, element_id, timeout=30):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, element_id))
    )

def wait_for_alert(driver, timeout=30):
    return WebDriverWait(driver, timeout).until(EC.alert_is_present())
