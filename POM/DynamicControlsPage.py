from Library import ConfigHandler
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec

class DynamicControlsClass:

    def __init__(self, obj):
        global driver, button_remove, button_enable, input_text, checkbox, button_add, button_disable
        driver = obj
        button_remove = ConfigHandler.readElementsData("DynamicControls", "remove")
        button_enable = ConfigHandler.readElementsData("DynamicControls", "enable")
        input_text = ConfigHandler.readElementsData("DynamicControls", "text")
        checkbox = ConfigHandler.readElementsData("DynamicControls", "checkbox")
        button_add = ConfigHandler.readElementsData("DynamicControls", "add")
        button_disable = ConfigHandler.readElementsData("DynamicControls", "disable")


    def mark_checkbox(self):
        WebDriverWait(driver,5).until(ec.presence_of_element_located((By.XPATH, checkbox)))
        mark = driver.find_element(By.XPATH, checkbox)
        mark.click()
        return mark

    def click_remove(self):
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, button_remove)))
        driver.find_element(By.XPATH, button_remove).click()

    def click_add(self):
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, button_add)))
        driver.find_element(By.XPATH, button_add).click()

    def click_enable(self):
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, button_enable)))
        driver.find_element(By.XPATH, button_enable).click()

    def click_disable(self):
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, button_disable)))
        driver.find_element(By.XPATH, button_disable).click()

    def write_to_input(self, text):
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH, input_text)))
        input = driver.find_element(By.XPATH, input_text)
        input.send_keys(text)
        return input

