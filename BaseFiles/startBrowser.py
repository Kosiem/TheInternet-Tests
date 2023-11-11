from selenium import webdriver
from Library import ConfigHandler


def startBrowserOnly():
    global driver
    choosen_browser = ConfigHandler.readUserBrowser()
    if choosen_browser == "Chrome":
        driver = webdriver.Chrome()
    elif choosen_browser == "Firefox":
        driver = webdriver.Firefox()
    elif choosen_browser == "Edge":
        driver = webdriver.Edge()
    else:
        raise NameError("Unsupported browser\n")
    return driver


def startBrowser(section, key):

    global driver
    choosen_browser = ConfigHandler.readUserBrowser()
    if choosen_browser == "Chrome":
        driver = webdriver.Chrome()
    elif choosen_browser == "Firefox":
        driver = webdriver.Firefox()
    elif choosen_browser == "Edge":
        driver = webdriver.Edge()
    else:
        raise NameError("Unsupported browser\n")

    choosen_url = ConfigHandler.readElementsData(section, key)
    driver.get(choosen_url)
    driver.maximize_window()
    return driver


