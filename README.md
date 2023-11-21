# TheInternet-Tests
Tests created for https://the-internet.herokuapp.com/, a special website where a number of elements are placed on which you can practice your testing skills in different scenarios. <br>
<br><br>

<h2>Project Structure</h2>
<b>The project's structure is divided into:</b><br><br>
- <b>Base Files</b> - a folder containing frequently recurring code - a function for opening the browser.<br><br>
<b>Example:</b>

```python
def startBrowserOnly():
    global driver
    choosen_browser = ConfigHandler.readUserBrowser()
    if choosen_browser == "Chrome":
        driver = webdriver.Chrome()
    elif choosen_browser == "Firefox":
        driver = webdriver.Firefox()
    elif choosen_browser == "Edge":
        driver = webdriver.Edge()
    else:
        raise NameError("Unsupported browser\n")
    return driver
```
- <b>Configs</b> - Config files in which the browser you wish to use is stored (Browser.cfg), as well as any necessary elements on the pages, stored in the form of XPATH (ElementsConfig.cfg)<br><br>
<b>Example:</b>
```python
[Hovers]
url=https://the-internet.herokuapp.com/hovers
figures=//div[@class='figure']
links=//div[@class='figure']/div/a
headers=//div[@class='figure']/div/h5
```
- <b>Library</b> - A folder with useful tools, a config parser, a test data generator, along with the files needed for some of these.<br><br>
<b>Example:</b>
```python
def readUserBrowser():
    browser_config = configparser.ConfigParser()
    browser_config.read("C:\\Users\\Patryk\\PycharmProjects\\The-Internet-Tests\\Configs\\Browser.cfg")
    return browser_config.get("Browser", "browser")
```

- <b>POM</b> - Page Objected Model - Each page that has been tested has been represented as a class, which contains methods corresponding to the functions on the page.<br><br>
<b>Example:</b>

```python
from Library import ConfigHandler
from selenium.webdriver.common.by import By
class JavaScriptAlertsClass:

    def __init__(self, obj):
        global driver, alert, confirm, prompt, result
        driver = obj
        alert = ConfigHandler.readElementsData("JSalert", "alert")
        confirm = ConfigHandler.readElementsData("JSalert", "confirm")
        prompt = ConfigHandler.readElementsData("JSalert", "prompt")
        result = ConfigHandler.readElementsData("JSalert", "msg")

    def click_alert(self):
        driver.find_element(By.XPATH, alert).click()

    def click_confirm(self):
        driver.find_element(By.XPATH, confirm).click()

    def click_prompt(self):
        driver.find_element(By.XPATH, prompt).click()

    def get_message(self):
        msg = driver.find_element(By.XPATH, result)
        return msg
```
- <b>TestCases</b> - A folder containing all the tests. There is one test per page, checking its functionality in many ways.
<b>Example</b>:
```python
def test_JS_Confirm_Dismiss(prepareEnv):
    testPage.click_confirm()
    alert = driver.switch_to.alert
    alert.dismiss()
    p = testPage.get_message()
    assert p.text == "You clicked: Cancel"
```

Each test has been described in terms of the steps to be taken during the test<br>
<b>Example:</b>

```python
"""
    <test_Enable_Disable_Enable_Input>
    Scenario: Click enable button, then disable input, and then enable it once again. Try to put data in input
    Steps:
        1. Click enable button
        2. Click disable button
        3. Click enable button
        4. Put data in input
        5. Check if written data is correct

"""
```


<h3>Allure Report</h3>
Using jenkins, I also generated an Allure report, for the tests

![image](https://github.com/Kosiem/TheInternet-Tests/assets/98033934/d31d03fa-1721-457f-ac35-6c7da9145fa9)


<h2>Tested pages</h2>
- ADD/REMOVE elements<br>
- BasicAuth<br>
- ChallengingDOM<br>
- CheckBoxes<br>
- ContextMenu<br>
- DigestAuth<br>
- DragAndDrop<br>
- DynamicControls<br>
- EntryAD<br>
- FileDownload<br>
- FileUpload<br>
- FormAuth<br>
- HorizontalSlider<br>
- Hovers<br>
- JQueryUI<br>
- JSalert<br>
- KeyPresses<br>
- StatusCodes<br>
