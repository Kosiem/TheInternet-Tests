import pytest
from BaseFiles import startBrowser
from Library import DataGenerator
from POM import FormAuthPage

@pytest.fixture()
def prepareEnv():
    global driver, testPage
    driver = startBrowser.startBrowser("FormAuth", "url")
    testPage = FormAuthPage.FormAuthClass(driver)
    driver.maximize_window()
    driver.delete_all_cookies()
    yield
    driver.close()


"""
    <test_Valid_Login>
    Scenario: Login with valid data
    Steps:
        1. Enter username
        2. Enter password
        3. Click login button
        4. Check if info message is correct
        5. Close info 
"""

def test_Valid_Login(prepareEnv):
    testPage.enter_username("tomsmith")
    testPage.enter_password("SuperSecretPassword!")
    testPage.login()
    info = testPage.get_info()

    assert info.text == 'You logged into a secure area!\n×'
    try:
        testPage.close_flash()
        assert True
    except:
        assert False


"""
    <test_Valid_Login_Logout_Login>
    Scenario: Login, logout, and login again
    Steps:
        1. Enter username
        2. Enter password
        3. Click login button
        4. Check if info message is correct
        5. Close info 
        6. Logout
        7. Check logout info
        8. Close info
        9. Repeat 1-5 steps
"""


def test_Valid_Login_Logout_Login(prepareEnv):
    testPage.enter_username("tomsmith")
    testPage.enter_password("SuperSecretPassword!")
    testPage.login()
    info = testPage.get_info()

    assert info.text == 'You logged into a secure area!\n×'
    try:
        testPage.close_flash()
        assert True
    except:
        assert False


    testPage.logout()
    info_logout = testPage.get_info()
    assert info_logout == " You logged out of the secure area!"
    try:
        testPage.close_flash()
        assert True
    except:
        assert False

    testPage.enter_username("tomsmith")
    testPage.enter_password("SuperSecretPassword!")
    testPage.login()
    info = testPage.get_info()

    assert info.text == 'You logged into a secure area!\n×'
    try:
        testPage.close_flash()
        assert True
    except:
        assert False


def test_Login_Only_Username(prepareEnv):
    testPage.enter_username("tomsmith")
    testPage.login()
    info = testPage.get_info()
    assert info.text == 'Your password is invalid!\n×'
    try:
        testPage.close_flash()
        assert True
    except:
        assert False

def test_Login_Only_Password(prepareEnv):
    testPage.enter_password("SuperSecretPassword!")
    testPage.login()
    info = testPage.get_info()
    assert info.text == 'Your username is invalid!\n×'
    try:
        testPage.close_flash()
        assert True
    except:
        assert False


def test_Login_Only_Button(prepareEnv):
    testPage.login()
    info = testPage.get_info()
    assert info.text == 'Your username is invalid!\n×'
    try:
        testPage.close_flash()
        assert True
    except:
        assert False


@pytest.mark.parametrize('data', DataGenerator.generateDataBasicAuth() )
def test_Login_Invalid_Data(prepareEnv, data):
    testPage.enter_username(data[0])
    testPage.enter_password(data[1])
    testPage.login()
    info = testPage.get_info()
    assert info.text == 'Your username is invalid!\n×'
    try:
        testPage.close_flash()
        assert True
    except:
        assert False
