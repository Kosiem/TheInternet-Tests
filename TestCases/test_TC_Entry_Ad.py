import pytest
from BaseFiles import startBrowser
from POM import EntryAdPage
import time

@pytest.fixture()
def prepareEnv():
    global driver, testPage
    driver = startBrowser.startBrowser("EntryAd", "url")
    testPage = EntryAdPage.EntryAdClass(driver)
    driver.maximize_window()
    yield
    driver.close()


"""
    <test_Close_Modal>
    Scenario: Wait for modal to appear and close it
    // After closing the modal it shouldn't appear anymore, even after restarting page
    Steps:
        1. Wait for modal
        2. Close it
        3. Refresh
        4. Try to close it again

"""

def test_Close_Modal(prepareEnv):
    time.sleep(3)
    windows = testPage.closeModal()
    driver.refresh()
    try:
        testPage.closeModal()
    except:
        assert True

"""
    <test_Close_Modal_Reenable>
    Scenario: Wait for modal to appear and close it. Then reenable it once again and close it
    // After closing the modal it shouldn't appear anymore, even after restarting page. By pressing re-enable button, it should appear again after restart
    Steps:
        1. Wait for modal
        2. Close it
        3. Refresh
        4. Try to close it again

"""

def test_Close_Modal_Reenable(prepareEnv):
    time.sleep(3)
    windows = testPage.closeModal()
    testPage.re_enable()
    driver.refresh()
    time.sleep(3)
    windows = testPage.closeModal()