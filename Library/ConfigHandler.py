import configparser

# Read data about elements locators


def readElementsData(section, key):
    config = configparser.ConfigParser()
    config.read("..\Configs\ElementsConfig.cfg")
    return config.get(section, key)

def readUserBrowser():
    browser_config = configparser.ConfigParser()
    browser_config.read("..\Configs\Browser.cfg")
    return browser_config.get("Browser", "browser")



print(readUserBrowser())