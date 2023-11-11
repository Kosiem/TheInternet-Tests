from Library import ConfigHandler
import requests
from requests.auth import HTTPDigestAuth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec

class DigestAuthClass:

    def __init__(self,obj):
        global driver, url
        driver = obj
        url = ConfigHandler.readElementsData("DigestAuth", "url")

    def basicpass(self, login, password):
        driver.get("https://" + login + ":" + password + "@the-internet.herokuapp.com/digest_auth")

    def statement(self):
        element = ConfigHandler.readElementsData("BasicAuth", "correct_login")
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, element)))
        loginMessage = driver.find_element(By.XPATH, ConfigHandler.readElementsData("BasicAuth", "correct_login"))
        return loginMessage

