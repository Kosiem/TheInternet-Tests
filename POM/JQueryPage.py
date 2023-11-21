from Library import ConfigHandler
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
import time
import os

class JQueryClass:

    def __init__(self, obj):
        global driver, list, mouse, download_directory
        driver = obj
        list = ConfigHandler.readElementsData("JQuery", "list")
        mouse = ActionChains(driver)
        download_directory = "C:\\Users\\Patryk\\Downloads"

    def select_disabled(self):
        disabled = driver.find_element(By.XPATH, list + "/li[1]")
        return disabled


    def download_pdf(self):
        script = "var elements = $('#menu'); var pdf = elements.find('#ui-id-5')[0]; var anchor = pdf.querySelector('a'); anchor.click();"
        driver.execute_script(script)
        time.sleep(5)
        path = os.path.join(download_directory, "menu.pdf")
        return path

    def download_csv(self):
        script = "var elements = $('#menu'); var pdf = elements.find('#ui-id-6')[0]; var anchor = pdf.querySelector('a'); anchor.click();"
        driver.execute_script(script)
        time.sleep(5)
        path = os.path.join(download_directory, "menu.csv")
        return path

    def download_excel(self):
        script = "var elements = $('#menu'); var pdf = elements.find('#ui-id-7')[0]; var anchor = pdf.querySelector('a'); anchor.click();"
        driver.execute_script(script)
        time.sleep(5)
        path = os.path.join(download_directory, "menu.xlsx")
        return path

    def back_to(self):
        script = "var elements = $('#menu'); var pdf = elements.find('#ui-id-8')[0]; var anchor = pdf.querySelector('a'); anchor.click();"
        driver.execute_script(script)
        WebDriverWait(driver, 5).until(ec.url_matches("https://the-internet.herokuapp.com/jqueryui"))

