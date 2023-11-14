import pytest
import time
from BaseFiles import startBrowser
from POM import HorizontalSliderPage

@pytest.fixture()
def prepareEnv():
    global driver, testPage
    driver = startBrowser.startBrowser("Slider", "url")
    testPage = HorizontalSliderPage.HorizonstalSliderClass(driver)
    driver.maximize_window()
    driver.delete_all_cookies()
    yield
    driver.close()


"""
    <test_Add_05_Value>
    Scenario: Move the slider by 0.5 value
    // When slider is focused, it automatically become 2.5 value
    Steps:
        1. Press right arrow on slider
        2. Check if value is equal to 3
"""

def test_Add_05_Value(prepareEnv):
    testPage.add_plus()
    assert testPage.get_value().text == "3"


"""
    <test_Minus_05_Value>
    Scenario: Move the slider by -0.5 value
    // When slider is focused, it automatically become 2.5 value
    Steps:
        1. Press left arrow on slider
        2. Check if value is equal to 2
"""


def test_Minus_05_Value(prepareEnv):
    testPage.add_minus()
    assert testPage.get_value().text == "2"


"""
    <test_Complex_Value_Scenario>
    Scenario: Perform more complex operations on slider
    // When slider is focused, it automatically become 2.5 value
    Steps:
        1. Press right arrow on slider
        2. Press right arrow on slider
        3. Press left arrow on slider
        4. Press left arrow on slider
        5. Press right arrow on slider
        6. Press left arrow on slider
        2. Check if value is equal to 2.5
"""


def test_Complex_Value_Sceniario(prepareEnv):
    testPage.add_plus()
    testPage.add_plus()
    time.sleep(2)
    testPage.add_minus()
    testPage.add_minus()
    testPage.add_plus()
    testPage.add_minus()

    assert testPage.get_value().text == "2.5"
