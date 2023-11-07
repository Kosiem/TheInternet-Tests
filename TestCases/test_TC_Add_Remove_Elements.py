import pytest
from selenium.webdriver.common.by import By

from BaseFiles import startBrowser
from Library import ConfigHandler


@pytest.fixture()
def returnSection():
    global section_name, new_element, div_element
    section_name = "AddRemoveElements"
    new_element = ConfigHandler.readElementsData(section_name, "click_button")
    div_element = ConfigHandler.readElementsData(section_name, "div_withNewElements")
    return section_name


"""
    Scenario: Add new element
    Steps:
        1. Click add button
        2. Check if new element exists

"""


def test_Add_New_Element(returnSection):
    driver = startBrowser.startBrowser(section_name, "url")
    driver.find_element(By.XPATH, new_element).click()
    added_element = driver.find_element(By.XPATH, div_element);
    assert added_element.is_displayed()
    assert added_element.text == "Delete"
    driver.close()


"""
    Scenario: Add three new elements
    Steps:
        1. Click add button three times
        2. Check if new elements exists

"""


def test_Add_Multiple_Elemets(returnSection):
    driver = startBrowser.startBrowser(section_name, "url")
    driver.find_element(By.XPATH, new_element).click()
    driver.find_element(By.XPATH, new_element).click()
    driver.find_element(By.XPATH, new_element).click()

    div_elements = driver.find_elements(By.XPATH, div_element)

    for element in div_elements:
        assert element.is_displayed()
        assert element.text == "Delete"

    driver.close()

    """
        Scenario: Add new element and delete it
        Steps:
            1. Click add button
            2. Click delete button
            3. Check if element is deleted
    """


def test_Add_Delete_Element(returnSection):
    driver = startBrowser.startBrowser(section_name, "url")
    driver.find_element(By.XPATH, new_element).click()

    driver.find_element(By.XPATH, div_element).click()

    try:
        driver.find_element(By.XPATH)
    except:
        assert True

    driver.close()

def test_Add_Delete_Multiple_Elemets(returnSection):
    driver = startBrowser.startBrowser(section_name, "url")
    driver.find_element()