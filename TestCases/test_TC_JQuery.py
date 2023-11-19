from BaseFiles import startBrowser
from POM import JQueryPage
import pytest
import os


@pytest.fixture()
def prepareEnv():
    global driver, testPage
    driver = startBrowser.startBrowser("JQuery", "url")
    testPage = JQueryPage.JQueryClass(driver)
    driver.maximize_window()
    yield
    driver.close()


"""
    <test_Check_Disabled>
    Scenario: Check if first element of UI is disabled
    Steps:
        1. Get disabled element
        2. Check if it is disabled
"""

def test_Check_Disabled(prepareEnv):
    disabled = testPage.select_disabled()
    assert disabled.get_attribute("aria-disabled") == "true"


"""
    <test_Download_PDF>
    Scenario: Check if by using UI, can download PDF file
    Steps:
        1. Get to element with download
        2. Check if file is downloaded
"""


def test_Download_PDF(prepareEnv):

    assert os.path.isfile(testPage.download_pdf())


"""
    <test_Download_CVS>
    Scenario: Check if by using UI, can download csv file
    Steps:
        1. Get to element with download
        2. Check if file is downloaded
"""


def test_Download_CSV(prepareEnv):

    assert os.path.isfile(testPage.download_csv())


"""
    <test_Download_Excel>
    Scenario: Check if by using UI, can download Excel file
    Steps:
        1. Get to element with download
        2. Check if file is downloaded
"""


def test_Download_Excel(prepareEnv):

    assert os.path.isfile(testPage.download_excel())

"""
    <test_Return_To_Main_Page>
    Scenario: Check if by using UI, can return to main page
    Steps:
        1. Get to element with main page link
        2. Click it, and check if url changed
"""


def test_Return_To_Main_Page(prepareEnv):
    testPage.back_to()
    assert driver.current_url == "https://the-internet.herokuapp.com/jqueryui"
