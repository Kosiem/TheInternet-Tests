import pytest
from BaseFiles import startBrowser
from POM import ContextMenuPage


@pytest.fixture()
def prepareEnv():
    global driver, testPage
    driver = startBrowser.startBrowser("ContextMenu", "url")
    testPage = ContextMenuPage.ContextMenuClass(driver)
    yield
    driver.close()


"""
    <test_Right_Click_On_Box>
    Scenario: Click right mouse button on box
    // the alert should be visible only after clicking right button of mouse
    Steps:
        1. Right-click on box
        2. Accept alert

"""


def test_Right_Click_On_Box(prepareEnv):
    testPage.right_click()
    assert testPage.accept_alert()


"""
    <test_Left_Click_On_Box>
    Scenario: Click left mouse button on box
    // the alert should be visible only after clicking right button of mouse
    Steps:
        1. Left-click on box
        2. Check if there is no alert

"""

def test_Left_Click_On_Box(prepareEnv):
    testPage.left_click()
    assert testPage.accept_alert() == False


"""
    <test_Keyboard_Click_On_Box>
    Scenario: Click Shift+F10 on box
    // the alert should be visible only after clicking right button of mouse
    // Shift + F10 is equal combination of context click to right mouse click
    Steps:
        1. Click Shift+F10 on box
        2. Check if there is no alert

"""


def test_Keyboard_Click_On_Box(prepareEnv):
    testPage.keyboard_click()
    assert testPage.accept_alert() == False
