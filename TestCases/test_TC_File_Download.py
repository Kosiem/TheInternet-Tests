import time

import pytest
from POM import FileDownloadPage
from BaseFiles import startBrowser
import os

@pytest.fixture()
def prepareEnv():
    global driver, testPage
    driver = startBrowser.startBrowser("FileDownload", "url")
    testPage = FileDownloadPage.FileDownloadClass(driver)
    driver.maximize_window()
    yield
    driver.close()


"""
    <test_Download_Certain_File>
    Scenario: Download file of certain name
    Steps:
        1. Download file
        2. Check if it is downloaded
"""


def test_Download_Certain_File(prepareEnv):
    testPage.download_file("selenium webdriverManagar.jpg")
    time.sleep(5)
    path = testPage.check_if_downloaded("selenium webdriverManagar.jpg")
    assert os.path.exists(path)

    os.remove(path)


"""
    <test_Download_Multiple_Files>
    Scenario: Download three files
    Steps:
        1. Download files
        2. Check if they are downloaded
"""


def test_Download_Multiple_Files(prepareEnv):
    testPage.download_file("first code.txt")
    testPage.download_file("people social network.png")
    testPage.download_file("LambdaTest.txt")

    time.sleep(8)
    path1 = testPage.check_if_downloaded("first code.txt")
    path2 = testPage.check_if_downloaded("people social network.png")
    path3 = testPage.check_if_downloaded("LambdaTest.txt")

    assert os.path.exists(path1)
    assert os.path.exists(path2)
    assert os.path.exists(path3)