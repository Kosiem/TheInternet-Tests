import pytest
from POM import DynamicControlsPage
from BaseFiles import startBrowser

@pytest.fixture()
def prepareEnv():
    global driver, testPage
    driver = startBrowser.startBrowser("DynamicControls", "url")
    testPage = DynamicControlsPage.DynamicControlsClass(driver)
    driver.maximize_window()
    yield
    driver.close()


"""
    <test_Mark_Checbkox>
    Scenario: Select checkbox
    Steps:
        1. Click checbkox
        2. Check if it is selected

"""


def test_Mark_Checbkox(prepareEnv):
    checkbox = testPage.mark_checkbox()
    assert checkbox.is_selected()


"""
    <test_Remove_Checkbox>
    Scenario: Click remove button
    Steps:
        1. Click remove button
        2. Try to mark checkbox

"""


def test_Remove_Checkbox(prepareEnv):
    testPage.click_remove()
    try:
        testPage.mark_checkbox()
    except:
        assert True


"""
    <test_Remove_Add_Checkbox>
    Scenario: Remove checkbox, add it again and click it
    Steps:
        1. Click remove button
        2. Click add button
        3. Mark checkbox
        4. Check if checkox is selected

"""

def test_Remove_Add_Checkbox(prepareEnv):
    testPage.click_remove()
    testPage.click_add()
    checbkox = testPage.mark_checkbox()
    assert checbkox.is_selected()


"""
    <test_Enable_Input>
    Scenario: Click enable button, and write some data to input
    Steps:
        1. Click enable button
        2. Write data to input
        3. Check if written data is correct

"""


def test_Enable_Input(prepareEnv):
    testPage.click_enable()
    input = testPage.write_to_input("admin123")
    assert input.get_attribute('value') == "admin123"


"""
    <test_Enable_Disable_Input>
    Scenario: Click enable button, then disable input, and try to put data in it
    Steps:
        1. Click enable button
        2. Click disable button
        3. Try to write data to input

"""

def test_Enable_Disable_Input(prepareEnv):
    testPage.click_enable()
    testPage.click_disable()
    try:
        testPage.write_to_input("admin123")
    except:
        assert True

"""
    <test_Enable_Disable_Enable_Input>
    Scenario: Click enable button, then disable input, and then enable it once again. Try to put data in input
    Steps:
        1. Click enable button
        2. Click disable button
        3. Click enable button
        4. Put data in input
        5. Check if written data is correct

"""

def test_Enable_Disable_Enable_Input(prepareEnv):
    testPage.click_enable()
    testPage.click_disable()
    testPage.click_enable()
    input = testPage.write_to_input("admin123")
    assert input.get_attribute('value') == "admin123"
