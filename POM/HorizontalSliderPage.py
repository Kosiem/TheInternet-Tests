from Library import ConfigHandler
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class HorizonstalSliderClass:

    def __init__(self, obj):
        global driver, input_slider, keyboard, slider, info, value
        driver = obj
        input_slider = ConfigHandler.readElementsData("Slider", "slider")
        keyboard = ActionChains(driver)
        slider = driver.find_element(By.XPATH, input_slider)
        info = driver.find_element(By.XPATH, ConfigHandler.readElementsData("Slider", "info"))
        self.value = 2.5

    def add_plus(self):
        keyboard.send_keys_to_element(slider, Keys.ARROW_RIGHT).perform()
        self.value += 0.5
        driver.execute_script("arguments[0].innerText=arguments[1]", info, self.value)


    def add_minus(self):
        keyboard.send_keys_to_element(slider, Keys.ARROW_LEFT).perform()
        self.value -= 0.5
        driver.execute_script("arguments[0].innerText=arguments[1]", info, self.value)

    def get_value(self):
        return info