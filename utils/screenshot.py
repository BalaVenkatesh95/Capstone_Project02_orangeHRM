# utils/screenshot.py
import os
from datetime import datetime

def take_screenshot(driver, folder="screenshots"):
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{timestamp}.png"
    filepath = os.path.join(folder, filename)
    driver.save_screenshot(filepath)
