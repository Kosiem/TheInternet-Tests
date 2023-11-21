from Library import ConfigHandler
from selenium.webdriver.common.by import By
class JavaScriptAlertsClass:

    def __init__(self, obj):
        global driver, alert, confirm, prompt, result
        driver = obj
        alert = ConfigHandler.readElementsData("JSalert", "alert")
        confirm = ConfigHandler.readElementsData("JSalert", "confirm")
        prompt = ConfigHandler.readElementsData("JSalert", "prompt")
        result = ConfigHandler.readElementsData("JSalert", "msg")

    def click_alert(self):
        driver.find_element(By.XPATH, alert).click()

    def click_confirm(self):
        driver.find_element(By.XPATH, confirm).click()

    def click_prompt(self):
        driver.find_element(By.XPATH, prompt).click()

    def get_message(self):
        msg = driver.find_element(By.XPATH, result)
        return msg