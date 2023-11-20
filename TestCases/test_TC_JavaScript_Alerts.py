from BaseFiles import startBrowser
from POM import JavaScriptAlertsPage
import pytest

@pytest.fixture()
def prepareEnv():
    global driver, testPage
    driver = startBrowser.startBrowser("JSalert", "url")
    testPage = JavaScriptAlertsPage.JavaScriptAlertsClass(driver)
    driver.maximize_window()
    yield
    driver.close()


"""
    <test_JS_Alert>
    Scenario: Get alert and confirm it
    Steps:
        1. Click JS Alert button
        2. Confirm alert
        3. Check result message
    
"""


def test_JS_Alert(prepareEnv):
    testPage.click_alert()
    alert = driver.switch_to.alert
    alert.accept()
    p = testPage.get_message()
    assert p.text == "You successfully clicked an alert"


"""
    <test_JS_Confirm>
    Scenario: Get confirm notification and confirm it
    Steps:
        1. Click JS Confirm button
        2. Confirm alert
        3. Check result message

"""


def test_JS_Confirm(prepareEnv):
    testPage.click_confirm()
    alert = driver.switch_to.alert
    alert.accept()
    p = testPage.get_message()
    assert p.text == "You clicked: Ok"


"""
    <test_JS_Confirm_Dismiss>
    Scenario: Get confirm notification and dismiss it
    Steps:
        1. Click JS Confirm button
        2. Dismiss alert
        3. Check result message

"""


def test_JS_Confirm_Dismiss(prepareEnv):
    testPage.click_confirm()
    alert = driver.switch_to.alert
    alert.dismiss()
    p = testPage.get_message()
    assert p.text == "You clicked: Cancel"


"""
    <test_JS_Prompt>
    Scenario: Get prompt alert and paste text to it
    Steps:
        1. Click JS Prompt button
        2. Send text to alert
        3. Confirm alert
        4. Check result message

"""


def test_JS_Prompt(prepareEnv):
    testPage.click_prompt()
    alert = driver.switch_to.alert
    alert.send_keys("Patryk")
    alert.accept()
    p = testPage.get_message()
    assert p.text == "You entered: Patryk"


"""
    <test_JS_Prompt_Dismiss>
    Scenario: Get prompt alert and paste text to it
    Steps:
        1. Click JS Prompt button
        2. Send text to alert
        3. Dismiss alert
        4. Check result message

"""


def test_JS_Prompt_Dismiss(prepareEnv):
    testPage.click_prompt()
    alert = driver.switch_to.alert
    alert.send_keys("Patryk")
    alert.dismiss()
    p = testPage.get_message()
    assert p.text == "You entered: null"


"""
    <test_JS_Prompt_Accept_Empty>
    Scenario: Get prompt alert and send it empty
    Steps:
        1. Click JS Prompt button
        2. Accept alert
        3. Check result message

"""


def test_JS_Prompt_Accept_Empty(prepareEnv):
    testPage.click_prompt()
    alert = driver.switch_to.alert
    alert.accept()
    p = testPage.get_message()
    assert p.text == "You entered:"