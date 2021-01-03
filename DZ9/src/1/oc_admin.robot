*** Settings ***
Library  OperatingSystem
Library  SeleniumLibrary
Library  AdvancedLogging
Library  DatabaseLibrary
Resource  ../Resources/AdminPage.robot
Suite Setup  Open Browser  NONE  ${BROWSER}
Suite Teardown  Close Browser

*** Test Cases ***
Scenario 1: I log in opencart as administrator
    Given that I open a browser on admin page
    When I enter my adminname and password
    And press Login button
    Then I should see that i logged in as administrator

Scenario 2: I adding an item to dashboard
    Given that I open a brouser on Products page
    When I press a button for adding item
    And then fill a table of item properties


*** Keywords ***
Verify Page Title Contains  [Arguments]  ${VALUE}
    ${TITLE}    Get Title
    Should Contain    ${TITLE}    ${VALUE}

that I open a browser on admin page
    Go To     ${OC_ADMINPAGE}

press Login button
    ${elem} =    Get WebElement    ${OC_ADMINPAGE_LOGIN_BUTTON_SELECTOR}
    ClickElement    ${elem}

I enter my adminname and password
    ${myHtml} =    Get Source
    Log    ${myHtml}    INFO  html = False
    ${elem} =    Get WebElement    ${OC_ADMINPAGE_USERNAME_SELECTOR}
    ClickElement    ${elem}
    InputText    ${elem}  ${ADMINNAME}
    ${elem} =    Get WebElement    ${OC_ADMINPAGE_PASSWORD_SELECTOR}
    ClickElement    ${elem}
    InputText    ${elem}  ${ADMINPASSWORD}

I should see that i logged in as administrator
    Verify Page Title Contains    ${OC_ADMINPAGE_TITLE_NEEDLE}
