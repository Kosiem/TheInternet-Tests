from selenium.webdriver.common.by import By

from Library import ConfigHandler


class AddRemoveElementsClass:
    def __init__(self, obj):
        global driver
        driver = obj

    def add_new_element(self):
        add = driver.find_element(By.XPATH, ConfigHandler.readElementsData("AddRemoveElements", "click_button"))
        add.click()
        return add

    def delete_elements(self):
        elements = driver.find_elements(By.XPATH,
                                        ConfigHandler.readElementsData("AddRemoveElements", "div_withNewElements"))
        for element in elements:
            element.click()

        return elements
