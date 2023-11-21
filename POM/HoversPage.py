from Library import ConfigHandler
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
class HoversClass:

    def __init__(self, obj):
        global driver, figures, links, headers, figures_elements, links_elements, headers_elements, mouse
        driver = obj
        figures = ConfigHandler.readElementsData("Hovers", "figures")
        links = ConfigHandler.readElementsData("Hovers", "links")
        headers = ConfigHandler.readElementsData("Hovers", "headers")

        figures_elements = driver.find_elements(By.XPATH, figures)
        links_elements = driver.find_elements(By.XPATH, links)
        headers_elements = driver.find_elements(By.XPATH, headers)

        mouse = ActionChains(driver)



    def hover_figure(self, number):
        mouse.move_to_element(figures_elements[number - 1]).perform()

    def get_link(self, number):
        return links_elements[number - 1]


    def get_header(self, number):
        return headers_elements[number - 1]