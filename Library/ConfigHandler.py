import configparser

# Read data about elements locators


def readElementsData(section, key):
    config = configparser.ConfigParser()
    config.read("C:\\Users\\Patryk\\PycharmProjects\\The-Internet-Tests\\Configs\\ElementsConfig.cfg")
    return config.get(section, key)

def readUserBrowser():
    browser_config = configparser.ConfigParser()
    browser_config.read("C:\\Users\\Patryk\\PycharmProjects\\The-Internet-Tests\\Configs\\Browser.cfg")
    return browser_config.get("Browser", "browser")



print(readUserBrowser())