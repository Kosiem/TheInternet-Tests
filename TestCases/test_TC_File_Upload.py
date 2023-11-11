import pytest
from BaseFiles import startBrowser
from POM import FileUploadPage

@pytest.fixture()
def prepareEnv():
    global driver, testPage
    driver = startBrowser.startBrowser("FileUpload", "url")
    testPage = FileUploadPage.FileUploadClass(driver)
    driver.maximize_window()
    yield
    driver.close()


"""
    <test_Upload_File>
    Scenario: Upload new file to server
    Steps:
        1. Upload new file
        2. Check if it got uploaded
"""

def test_Upload_File(prepareEnv):
    testPage.file_upload("..\\Library\\test_uploadfile.txt")
    testPage.click_upload()
    message = testPage.check_message()
    file_name = testPage.check_file_name()

    assert message.text == "File Uploaded!"
    assert file_name.text == "test_uploadfile.txt"