from Library import ConfigHandler
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class DragAndDropClass:

    def __init__(self, obj):
        global driver, div1, div2, mouse
        driver = obj
        div1 = ConfigHandler.readElementsData("DragAndDrop", "div1")
        div2 = ConfigHandler.readElementsData("DragAndDrop", "div2")
        mouse = ActionChains(driver)

    def drag_a_to_b(self):
        div1_box = driver.find_element(By.XPATH, div1)
        div2_box = driver.find_element(By.XPATH, div2)
        mouse.drag_and_drop(div1_box, div2_box).perform()

    def drag_b_to_a(self):
        div1_box = driver.find_element(By.XPATH, div1)
        div2_box = driver.find_element(By.XPATH, div2)
        mouse.drag_and_drop(div2_box, div1_box).perform()

    def return_a(self):
        return driver.find_element(By.XPATH, div1)

    def return_b(self):
        return driver.find_element(By.XPATH, div2)