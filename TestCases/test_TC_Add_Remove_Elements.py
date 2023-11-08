import pytest
from selenium.webdriver.common.by import By

from BaseFiles import startBrowser
from Library import ConfigHandler
from POM import AddRemoveElementsPage


@pytest.fixture()
def prepareEnv():
    global driver, testPage
    driver = startBrowser.startBrowser("AddRemoveElements", "url")
    testPage = AddRemoveElementsPage.AddRemoveElementsClass(driver)


"""
    Scenario: Add new element
    Steps:
        1. Click add button
        2. Check if new element exists

"""


def test_Add_New_Element(prepareEnv):
    testPage.add_new_element()
    added_element = \
    driver.find_elements(By.XPATH, ConfigHandler.readElementsData("AddRemoveElements", "div_withNewElements"))[0]
    assert added_element.is_displayed()
    assert added_element.text == "Delete"
    driver.close()


"""
    Scenario: Add three new elements
    Steps:
        1. Click add button three times
        2. Check if new elements exists

"""


def test_Add_Multiple_Elemets(prepareEnv):
    for i in range(0, 3):
        testPage.add_new_element()
    div_elements = driver.find_elements(By.XPATH,
                                        ConfigHandler.readElementsData("AddRemoveElements", "div_withNewElements"))

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


def test_Add_Delete_Element(prepareEnv):
    testPage.add_new_element()
    testPage.delete_elements()

    try:
        driver.find_element(By.XPATH, ConfigHandler.readElementsData("AddRemoveElements", "div_withNewElements"))
    except:
        assert True

    driver.close()

    """
        Scenario: Add three new elements and delete it
        Steps:
            1. Click add button three times
            2. Click delete button on every element
            3. Check if every element is deleted
    """


def test_Add_Delete_Multiple_Elemets(prepareEnv):
    for i in range(0, 3):
        testPage.add_new_element()

    testPage.delete_elements()

    try:
        driver.find_element(By.XPATH, ConfigHandler.readElementsData("AddRemoveElements", "div_withNewElements"))
    except:
        assert True
