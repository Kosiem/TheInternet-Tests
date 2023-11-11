from Library import ConfigHandler
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec

class FileUploadClass:

    def __init__(self, obj):
        global driver, input_file, message, file_name, upload
        driver = obj
        input_file = ConfigHandler.readElementsData("FileUpload", "input_file")
        message = ConfigHandler.readElementsData("FileUpload", "message")
        file_name = ConfigHandler.readElementsData("FileUpload", "file_name")
        upload = ConfigHandler.readElementsData("FileUpload", "upload")


    def file_upload(self, path):
        driver.find_element(By.XPATH, input_file).send_keys(os.path.abspath(path))

    def click_upload(self):
        driver.find_element(By.XPATH, upload).click()

    def check_message(self):
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, message)))
        header = driver.find_element(By.XPATH, message)
        return header

    def check_file_name(self):
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, file_name)))
        file = driver.find_element(By.XPATH, file_name)
        return file
