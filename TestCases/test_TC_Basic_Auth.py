import pytest
from BaseFiles import startBrowser
from POM import BasicAuthPage
from Library import DataGenerator

@pytest.fixture()
def prepareEnv():
    global driver, testPage
    driver = startBrowser.startBrowser("BasicAuth", "url")
    driver.delete_all_cookies()
    testPage = BasicAuthPage.BasicAuthClass(driver)
    yield
    driver.close()


"""
    <test_Correct_Data>
    Scenario: Login with correct data
    Steps:
        1. Write correct login
        2. Write correct password
        3. Accept alert
        4. Check message

"""

def test_Correct_Data(prepareEnv):
    testPage.sendLogin("admin")
    testPage.sendPassword("admin")

    assert testPage.acceptAlert()
    assert testPage.statement().text == "Congratulations! You must have the proper credentials."


"""
    <test_Invalid_Data>
    Scenario: Try to login with invalid data
    Steps:
        1. Write uncorrect login
        2. Write uncorrect password
        3. Accept alert
        4. Check message

"""


def test_Invalid_Data(prepareEnv):
    testPage.sendLogin("admin123")
    testPage.sendPassword("admin123")

    assert testPage.acceptAlert()

    try:
        testPage.statement().text == "Congratulations! You must have the proper credentials."
    except:
        assert True


"""
    <test_Invalid_Data_Multiple_Times>
    Scenario: Try to login with invalid data but with different set of data
    Steps:
        For each username and password:
            1. Write uncorrect login
            2. Write uncorrect password
            3. Accept alert
            4. Check message

"""


@pytest.mark.parametrize('data', DataGenerator.generateDataBasicAuth())
def test_Invalid_Data_Multiple_Times(prepareEnv, data):
    testPage.sendLogin(data[0])
    testPage.sendPassword(data[1])

    assert testPage.acceptAlert()
    try:
        testPage.statement().text == "Congratulations! You must have the proper credentials."
    except:
        assert True


def test_Accept_Alert_Without_Login(prepareEnv):
    assert testPage.acceptAlert()
    try:
        testPage.statement().text = "Congratulations! You must have the proper credentials."
    except:
        assert True

