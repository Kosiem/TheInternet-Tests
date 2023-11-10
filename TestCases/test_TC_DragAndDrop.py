import pytest
from BaseFiles import startBrowser
from POM import DragAndDropPage

@pytest.fixture()
def prepareEnv():
    global driver, testPage
    driver = startBrowser.startBrowser("DragAndDrop", "url")
    testPage = DragAndDropPage.DragAndDropClass(driver)
    yield
    driver.close()

"""
    <test_Move_A_To_B>
    Scenario: Drag and drop div A to div B
    // After drop, the innerText of div A should be equal to B, and div B to A
    Steps:
        1. Drag and drop A to B
        2. Check inner text of div A
        3. Check inner text of div B

"""

def test_Move_A_To_B(prepareEnv):
    testPage.drag_a_to_b()
    divA = testPage.return_a()
    divB = testPage.return_b()

    assert divA.text == "B"
    assert divB.text == "A"


"""
    <test_Move_B_To_A>
    Scenario: Drag and drop div A to div B
    // After drop, the innerText of div A should be equal to B, and div B to A
    Steps:
        1. Drag and drop B to A
        2. Check inner text of div A
        3. Check inner text of div B

"""

def test_Move_B_To_A(prepareEnv):
    testPage.drag_b_to_a()
    divA = testPage.return_a()
    divB = testPage.return_b()

    assert divA.text == "B"
    assert divB.text == "A"

"""
    <test_Move_B_To_A>
    Scenario: Drag and drop multiple times
    // After drop, the innerText of div A should be equal to B, and div B to A
    Steps:
        1. Drag and drop A to B
        2. Drag and drop B to A
        3. Drag and drop B to A
        4. Drag and drop A to B
        5. Check inner text of div A
        6. Check inner text of div B
"""

def test_Complex_Scenario(prepareEnv):
    testPage.drag_a_to_b()
    testPage.drag_b_to_a()
    testPage.drag_b_to_a()
    testPage.drag_a_to_b()

    divA = testPage.return_a()
    divB = testPage.return_b()

    assert divA.text == "A"
    assert divB.text == "B"

