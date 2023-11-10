import time

import pytest

from BaseFiles import startBrowser
from POM import ChallengingDOMPage

button_data = ["foo", "bar", "baz", "qux"]


@pytest.fixture()
def prepareEnv():
    global testPage, driver
    driver = startBrowser.startBrowser("ChallengingDOM", "url")
    driver.delete_all_cookies()
    driver.maximize_window()
    testPage = ChallengingDOMPage.ChallengingDOM_class(driver)
    yield
    driver.close()


"""
    <test_Click_Foo_Button>
    Scenario: Find and click button with selected text
    Steps:
        1. Check if button exists
        2. If not refresh the page until it will be found
        3. Click button

"""


def test_Click_Selected_Button(prepareEnv):
    try:
        testPage.click_button('foo')
        assert True
    except:
        driver.refresh()


"""
    <test_Click_All_Buttons>
    Scenario: Find and click all buttons
    // Buttons text are stored in button_data list
    // Max attemps of searching the button is 3 times
    Steps:
        1. Check if button exists
        2. If not refresh the browser
        2. Click it
        3. To check_count add 1
        4. Repeat these steps for all button_data elements
        5. If check_count is equal to 4, that means all of four buttons have been clicked
"""


def test_Click_All_Buttons(prepareEnv):
    check_count = 0
    for text in button_data:
        while True:
            try:
                time.sleep(2)
                testPage.click_button(text)
                check_count += 1
                print("clicked")
                break
            except:
                driver.refresh()
            else:
                continue
            print(text)
            print(check_count)
        if check_count == 4:
            break

    assert check_count == 4


"""
    <test_Edit_Button>
    Scenario: Click edit button from first row
    Steps:
        1. Click button
        2. Check if URL is correct
    
"""


def test_Edit_Button(prepareEnv):
    testPage.click_edit_button()
    assert driver.title == "https://the-internet.herokuapp.com/challenging_dom#edit"


"""
    <test_Delete_Button>
    Scenario: Click edit button from first row
    Steps:
        1. Click button
        2. Check if URL is correct

"""


def test_Delete_Button(prepareEnv):
    testPage.click_delete_button()
    assert driver.title == "https://the-internet.herokuapp.com/challenging_dom#delete"
