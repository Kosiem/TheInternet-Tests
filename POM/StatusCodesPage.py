from Library import ConfigHandler
from selenium.webdriver.common.by import By

class StatusCodesClass:

    def __init__(self, obj):
        global driver, status_200, status_301, status_404, status_500
        driver = obj
        status_200 = driver.find_element(By.XPATH, ConfigHandler.readElementsData("StatusCodes", "200"))
        status_301 = driver.find_element(By.XPATH, ConfigHandler.readElementsData("StatusCodes", "301"))
        status_404 = driver.find_element(By.XPATH, ConfigHandler.readElementsData("StatusCodes", "404"))
        status_500 = driver.find_element(By.XPATH, ConfigHandler.readElementsData("StatusCodes", "500"))

    def click_status_200(self):
        status_200.click()

    def click_status_301(self):
        status_301.click()

    def click_status_404(self):
        status_404.click()

    def click_status_500(self):
        status_500.click()

