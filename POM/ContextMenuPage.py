from Library import ConfigHandler
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ContextMenuClass:

    def __init__(self, obj):
        global driver, mouse, box
        driver = obj
        mouse = ActionChains(driver)
        box = ConfigHandler.readElementsData("ContextMenu", "box")


    def right_click(self):
        box_place = driver.find_element(By.XPATH, box)
        mouse.move_to_element(box_place).context_click().perform()

    def left_click(self):
        box_place = driver.find_element(By.XPATH, box)
        mouse.move_to_element(box_place).click().perform()

    def keyboard_click(self):
        box_place = driver.find_element(By.XPATH, box)
        keyboard = ActionChains(driver)
        keyboard.move_to_element(box_place).key_down(Keys.SHIFT).send_keys_to_element(box_place, Keys.F10).perform()

    def accept_alert(self):
        try:
            alert = driver.switch_to.alert
            alert.accept()
            return True
        except:
            return False