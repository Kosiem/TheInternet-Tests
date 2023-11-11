from Library import ConfigHandler
from selenium.webdriver.common.by import By
class FormAuthClass:

    def __init__(self, obj):
        global driver, username, password, login, flash_div, close_flash, logout
        driver = obj
        username = ConfigHandler.readElementsData("FormAuth","username")
        password = ConfigHandler.readElementsData("FormAuth","password")
        login = ConfigHandler.readElementsData("FormAuth","login")
        flash_div = ConfigHandler.readElementsData("FormAuth","flash_div")
        close_flash = ConfigHandler.readElementsData("FormAuth","close_flash")
        logout = ConfigHandler.readElementsData("FormAuth","logout")

    def enter_username(self, user):
        driver.find_element(By.XPATH, username).send_keys(user)

    def enter_password(self, passw):
        driver.find_element(By.XPATH, password).send_keys(passw)

    def login(self):
        driver.find_element(By.XPATH, login).click()

    def get_info(self):
        flash = driver.find_element(By.XPATH, flash_div)
        return flash

    def close_flash(self):
        driver.find_element(By.XPATH, close_flash).click()

    def logout(self):
        driver.find_element(By.XPATH, logout).click()