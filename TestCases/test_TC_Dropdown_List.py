import pytest
from BaseFiles import startBrowser
from POM import DropdownPage

@pytest.fixture()
def prepareEnv():
    global driver, testPage
    driver = startBrowser.startBrowser("Dropdown", "url")
    testPage = DropdownPage.DrodpdownPageClass(driver)
    driver.maximize_window()
    yield
    driver.close()


"""
    <test_Select_First_Option>
    Scenario: Select first option from list
    Steps:
        1. Select first option
        2. Check if it is selected
        3. Check if option value is equal to "Option 1"

"""



def test_Select_First_Option(prepareEnv):
    testPage.select_option1()
    selected = testPage.option()
    assert selected.is_selected()
    assert selected.text == "Option 1"

"""
    <test_Select_Second_Option>
    Scenario: Select second option from list
    Steps:
        1. Select second option
        2. Check if it is selected
        3. Check if option value is equal to "Option 2"

"""

def test_Select_Second_Option(prepareEnv):
    testPage.select_option2()
    selected = testPage.option()
    assert selected.is_selected()
    assert selected.text == "Option 2"

"""
    <test_Check_Default_Option>
    Scenario: Check the default option selected in list
    // default option got attribute disabled
    Steps:
        1. Check if it is selected
        2. Check if option value is equal to "Please select an option"

"""


def test_Check_Default_Option(prepareEnv):
    selected = testPage.option()
    assert selected.get_attribute("disabled")
    assert selected.is_selected()
    assert selected.text == "Please select an option"
