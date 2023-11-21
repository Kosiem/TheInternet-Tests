from Library import ConfigHandler
from selenium.webdriver.common.by import By

class KeyPressesClass:

    def __init__(self, obj):
        global driver, input, result
        driver = obj
        input = driver.find_element(By.XPATH, ConfigHandler.readElementsData("KeyPresses", "input"))
        result = driver.find_element(By.XPATH, ConfigHandler.readElementsData("KeyPresses", "msg"))

    def send_key(self, key):
        input.send_keys(key)

    def get_message(self):
        return result

