import pytest
from BaseFiles import startBrowser
from POM import HoversPage
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By


@pytest.fixture()
def prepareEnv():
    global driver, testPage
    driver = startBrowser.startBrowser("Hovers", "url")
    testPage = HoversPage.HoversClass(driver)
    driver.maximize_window()
    yield
    driver.close()


"""
    <test_User_One_Hover>
    Scenario: Hover mouse at user one, and check it elements
    // User1 - id = 1, User2 - id = 2, User3 - id = 3
    Steps:
        1. Move mouse to user one
        2. Check if user name is user1
        3. Check if there is link to user1 profile
        4. Check if it's clickable
"""

def test_User_One_Hover(prepareEnv):
    testPage.hover_figure(1)
    header = testPage.get_header(1)

    assert header.text == "name: user1"

    link = testPage.get_link(1)

    assert link.get_attribute("href") == "https://the-internet.herokuapp.com/users/1"

"""
    <test_User_Two_Hover>
    Scenario: Hover mouse at user two, and check it elements
    // User1 - id = 1, User2 - id = 2, User3 - id = 3
    Steps:
        1. Move mouse to user two
        2. Check if user name is user2
        3. Check if there is link to user2 profile
        4. Check if it's clickable
"""

def test_User_Two_Hover(prepareEnv):
    testPage.hover_figure(2)
    header = testPage.get_header(2)

    assert header.text == "name: user2"

    link = testPage.get_link(2)

    assert link.get_attribute("href") == "https://the-internet.herokuapp.com/users/2"

    """
        <test_User_Three_Hover>
        Scenario: Hover mouse at user three, and check it elements
        // User1 - id = 1, User2 - id = 2, User3 - id = 3
        Steps:
            1. Move mouse to user three
            2. Check if user name is user3
            3. Check if there is link to user3 profile
            4. Check if it's clickable
    """


def test_User_Three_Hover(prepareEnv):
    testPage.hover_figure(3)
    header = testPage.get_header(3)

    assert header.text == "name: user3"

    link = testPage.get_link(3)

    assert link.get_attribute("href") == "https://the-internet.herokuapp.com/users/3"


"""
    <test_Hover_All_Users>
    Scenario: Hover mouse at every user, and check it elements
    // User1 - id = 1, User2 - id = 2, User3 - id = 3
    Steps:
        1. Move mouse to user 
        2. Check if user name is proper
        3. Check if there is link to user profile
        4. Check if it's clickable
        5. Repeat it for every user
"""

def test_Hover_All_Users(prepareEnv):

    testPage.hover_figure(1)
    header = testPage.get_header(1)

    assert header.text == "name: user1"

    link = testPage.get_link(1)

    assert link.get_attribute("href") == "https://the-internet.herokuapp.com/users/1"

    testPage.hover_figure(2)
    header = testPage.get_header(2)

    assert header.text == "name: user2"

    link = testPage.get_link(2)

    assert link.get_attribute("href") == "https://the-internet.herokuapp.com/users/2"

    testPage.hover_figure(3)
    header = testPage.get_header(3)

    assert header.text == "name: user3"

    link = testPage.get_link(3)

    assert link.get_attribute("href") == "https://the-internet.herokuapp.com/users/3"
