from Library import ConfigHandler
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class CheckboxesClass:
    def __init__(self, obj):
        global driver, checkbox1, checkbox2, mouse
        driver = obj
        checkbox1 = ConfigHandler.readElementsData("Checkboxes", "checkbox1")
        checkbox2 = ConfigHandler.readElementsData("Checkboxes", "checkbox2")
        mouse = ActionChains(driver)

    def click_checkbox1(self):
        chk1 = driver.find_element(By.XPATH, checkbox1)
        mouse.move_to_element(chk1).click().perform()
        return chk1


    def click_checkbox2(self):
        mouse = ActionChains(driver)
        chk2 = driver.find_element(By.XPATH, checkbox2)
        mouse.move_to_element(chk2).click().perform()
        return chk2
