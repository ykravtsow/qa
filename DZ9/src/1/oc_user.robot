*** Settings ***
Library  OperatingSystem
Library  SeleniumLibrary
Library  AdvancedLogging
Resource  ../Resources/MainPage.robot
Suite Setup  Open Browser  NONE  ${BROWSER}
Suite Teardown  Close Browser

*** Test Cases ***
Scenario 1: I log in opencart as a user
    Given that I open a browser on main page
    When I enter my username and password
    And press Login button
    Then I should see that i logged in

Scenario 2: I buying an item
    Given that I open a browser on main page
    When I select Monitor from menu



*** Keywords ***
that I open a browser on main page
    Go To     ${OC_MAINPAGE}

I enter my username and password
    ${myHtml} =    Get Source
    Log    ${myHtml}    INFO  html = False
    ${elem} =    Get WebElement    ${OC_MAINPAGE_ACCOUNT_SELECTOR}
    ClickElement    ${elem}
    ${elem} =    Get WebElement    ${OC_MAINPAGE_LOGIN_SELECTOR}
    ClickElement    ${elem}
    ${elem} =    Get WebElement    ${OC_LOGIN_EMAIL_SELECTOR}
    ClickElement    ${elem}
    InputText    ${elem}  ${USERMAIL}
    ${elem} =    Get WebElement    ${OC_LOGIN_PASSWORD_SELECTOR}
    ClickElement    ${elem}
    InputText    ${elem}  ${PASSWORD}

press Login button
    ${elem} =    Get WebElement    ${OC_LOGIN_LOGIN_BUTTON_SELECTOR}
    ClickElement    ${elem}

I should see that i logged in
    Verify Page Title Contains    ${OC_LOGIN_TITLE_NEEDLE}


Verify Page Title Contains   [Arguments]  ${VALUE}
    ${TITLE}    Get Title
    Should Contain    ${TITLE}    ${VALUE}


