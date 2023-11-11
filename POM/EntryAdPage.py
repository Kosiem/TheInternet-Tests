from Library import ConfigHandler
from selenium.webdriver.common.by import By

class EntryAdClass():

    def __init__(self, obj):
        global driver, re_enable
        driver = obj
        re_enable = ConfigHandler.readElementsData("EntryAd", "re_enable")

    def closeModal(self):
        current_url = ConfigHandler.readElementsData("EntryAd", "url")
        allWindows = driver.window_handles
        print(allWindows, flush=True)
        for window in allWindows:
            driver.switch_to.window(window)
            if driver.current_url == current_url:
                mainWindow = window
            else:
                print("closing popup")
                driver.close()

        driver.switch_to.window(mainWindow)
        return allWindows

    def re_enable(self):
        driver.find_element(By.XPATH, re_enable).click
