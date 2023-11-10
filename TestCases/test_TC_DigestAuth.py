
# Tests Copied from test_TC_Basic_Auth

import pytest

from BaseFiles import startBrowser
from Library import DataGenerator
from POM import DigestAuthPage


@pytest.fixture()
def prepareEnv():
    global testPage, driver
    driver = startBrowser.startBrowserOnly()
    testPage = DigestAuthPage.DigestAuthClass(driver)
    yield
    driver.close()


"""
    <test_Correct_Data>
    Scenario: Login with correct data
    Steps:
        1. Send https link with correct data
        2. Check if login message appears

"""


def test_Correct_Data(prepareEnv):
    testPage.basicpass("admin", "admin")
    assert testPage.statement().text == "Congratulations! You must have the proper credentials."


"""
    <test_Invalid_Data>
    Scenario: Try to login with invalid data
    Steps:
        1. Send https link with uncorrect data
        2. Check if user is not logged in

"""


def test_Invalid_Data(prepareEnv):
    testPage.basicpass("admin123", "admin123")
    try:
        testPage.statement().text == "Congratulations! You must have the proper credentials."
    except:
        assert True


"""
    <test_Invalid_Data_Multiple_Times>
    Scenario: Try to login with invalid data but with different set of data
    Steps:
        For each username and password:
            1. Send https link with uncorrect data
            2. Check if user is not logged in

"""


@pytest.mark.parametrize('data', DataGenerator.generateDataBasicAuth())
def test_Invalid_Data_Multiple_Times(prepareEnv, data):
    testPage.basicpass(data[0], data[1])

    try:
        testPage.statement().text == "Congratulations! You must have the proper credentials."
    except:
        assert True
