from Library import ConfigHandler
import os
from selenium.webdriver.common.by import By


class FileDownloadClass:

    def __init__(self,obj):
        global driver, files
        driver = obj
        files = ConfigHandler.readElementsData("FileDownload", "files")


    def download_file(self, filename):
        all_files = driver.find_elements(By.XPATH, files)
        for i in all_files:
            if i.text == filename:
                i.click()

    def check_if_downloaded(self, filename):
        download_directory = "C:\\Users\\Patryk\\Downloads"
        full_path = os.path.join(download_directory, filename)
        return full_path