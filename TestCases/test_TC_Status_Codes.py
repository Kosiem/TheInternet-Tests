from BaseFiles import startBrowser
from POM import StatusCodesPage
import pytest
import requests

@pytest.fixture()
def prepareEnv():
    global driver, testPage
    driver = startBrowser.startBrowser("StatusCodes", "url")
    testPage = StatusCodesPage.StatusCodesClass(driver)
    driver.maximize_window()
    yield
    driver.close()


"""
    <test_Status_200>
    Scenario: Test status codes
    Steps:
        1. Click button with redirection
        2. Check if status code is equal to 200

"""


def test_Status_200(prepareEnv):
    testPage.click_status_200()
    url = driver.current_url
    response = requests.get(url)
    status = response.status_code

    assert status == 200


"""
    <test_Status_301>
    Scenario: Test status codes
    Steps:
        1. Click button with redirection
        2. Check if status code is equal to 301

"""


def test_Status_301(prepareEnv):
    testPage.click_status_301()
    url = driver.current_url
    response = requests.get(url)
    status = response.status_code

    assert status == 301


"""
    <test_Status_404>
    Scenario: Test status codes
    Steps:
        1. Click button with redirection
        2. Check if status code is equal to 404

"""


def test_Status_404(prepareEnv):
    testPage.click_status_404()
    url = driver.current_url
    response = requests.get(url)
    status = response.status_code

    assert status == 404


"""
    <test_Status_500>
    Scenario: Test status codes
    Steps:
        1. Click button with redirection
        2. Check if status code is equal to 500

"""


def test_Status_500(prepareEnv):
    testPage.click_status_500()
    url = driver.current_url
    response = requests.get(url)
    status = response.status_code

    assert status == 500