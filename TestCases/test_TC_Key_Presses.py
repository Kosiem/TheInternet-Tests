import time

from BaseFiles import startBrowser
from POM import KeyPressesPage
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture()
def prepareEnv():
    global driver, testPage
    driver = startBrowser.startBrowser("KeyPresses", "url")
    testPage = KeyPressesPage.KeyPressesClass(driver)
    driver.maximize_window()
    yield
    driver.close()


"""
    <test_Send_Normal_Keys>
    Scenario: Paste keys to input
    Steps:
        1. Paste letter 'P' to input
        2. Check if result message is correct
        3. Repeat these steps for every letter

"""


def test_Send_Normal_Keys(prepareEnv):
    testPage.send_key('P')
    result = testPage.get_message()
    assert result.text == "You entered: P"
    testPage.send_key('Y')
    result = testPage.get_message()
    assert result.text == "You entered: Y"
    testPage.send_key("T")
    result = testPage.get_message()
    assert result.text == "You entered: T"
    testPage.send_key("H")
    result = testPage.get_message()
    assert result.text == "You entered: H"
    testPage.send_key("O")
    result = testPage.get_message()
    assert result.text == "You entered: O"
    testPage.send_key("N")
    result = testPage.get_message()
    assert result.text == "You entered: N"


"""
    <test_Send_Normal_Keys>
    Scenario: Paste keys to input
    Steps:
        1. Paste special key to input
        2. Check if message is correct
        3. Repeat this steps for every key

"""


def test_Send_Special_Keys(prepareEnv):
    testPage.send_key(Keys.CONTROL)
    result = testPage.get_message()
    assert result.text == "You entered: CONTROL"
    testPage.send_key(Keys.TAB)
    result = testPage.get_message()
    assert result.text == "You entered: TAB"
    testPage.send_key(Keys.ESCAPE)
    result = testPage.get_message()
    assert result.text == "You entered: ESCAPE"
    testPage.send_key(Keys.HOME)
    result = testPage.get_message()
    assert result.text == "You entered: HOME"