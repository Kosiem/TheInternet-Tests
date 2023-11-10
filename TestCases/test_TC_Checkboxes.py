import pytest

from BaseFiles import startBrowser
from POM import CheckboxesPage


@pytest.fixture()
def prepareEnv():
    global driver, testPage
    driver = startBrowser.startBrowser("Checkboxes", "url")
    driver.delete_all_cookies()
    testPage = CheckboxesPage.CheckboxesClass(driver)
    yield
    driver.close()


"""
    <test_Click_First_Checbkox>
    Scenario: Click first checkbox
    // The second checkbox is clicked by default
    Steps:
        1. Click first checkbox
        2. Unclick second checkbox
        3. Check if first checbkox is marked, and second is not

"""


def test_Click_First_Checkbox(prepareEnv):
    chk1 = testPage.click_checkbox1()
    chk2 = testPage.clickCheckbox2()
    assert chk1.is_selected()
    assert chk2.is_selected() == False


"""
    <test_Click_Second_Checkbox>
    Scenario: Click Second checkbox
    // The second checkbox is clicked by default
    Steps:
        1. Unclick second checkbox
        2. Click second checkbox
        3. Check if second checkbox is marked

"""


def test_Click_Second_Checkbox(prepareEnv):
    chk2 = testPage.click_checkbox2()
    testPage.click_checkbox2()
    assert chk2.is_selected()


"""
    <test_Click_Both_Checkboxes>
    Scenario: Click both checkboxes
    // The second checkbox is clicked by default
    Steps:
        1. Click first checkbox
        2. Unclick second checkbox
        3. Click second checkbox
        4. Check if both of them are marked
"""


def test_Click_Both_Checkboxes(prepareEnv):
    chk1 = testPage.click_checkbox1()
    chk2 = testPage.click_checkbox2()
    testPage.click_checkbox2()
    assert chk1.is_selected()
    assert chk2.is_selected()
