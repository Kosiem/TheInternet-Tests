from Library import ConfigHandler
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class ChallengingDOM_class:

    def __init__(self, obj):
        global driver, mouse, buttons
        driver = obj
        buttons = ConfigHandler.readElementsData("ChallengingDOM","buttons")
        mouse = ActionChains(driver)

    def get_buttons(self):
        list_buttons = driver.find_elements(By.XPATH, buttons)
        return list_buttons

    def click_button(self, innerText):
        list_buttons = self.get_buttons()
        for button in list_buttons:
            print("button: " + button.text)
            if button.text == innerText:
                mouse.move_to_element(button)
                button.click()
                self.get_buttons()

    def click_edit_button(self):
        driver.find_element(By.XPATH, ConfigHandler.readElementsData("ChallengingDom", "edit_button")).click()

    def click_delete_button(self):
        driver.find_element(By.XPATH, ConfigHandler.readElementsData("ChallengingDom", "edit_button")).click()
