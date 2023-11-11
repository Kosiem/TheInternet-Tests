from Library import ConfigHandler
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DrodpdownPageClass:

    def __init__(self, obj):
        global driver, select
        driver = obj
        select = driver.find_element(By.XPATH, ConfigHandler.readElementsData("Dropdown", "select"))
        select = Select(select)


    def select_option1(self):
        select.select_by_value("1")

    def select_option2(self):
        select.select_by_value("2")

    def option(self):
       return select.first_selected_option



