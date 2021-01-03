*** Settings ***
Resource  Variables.robot

*** Variables ***
${USERMAIL}    user@example.com
${PASSWORD}    testtest
${OC_MAINPAGE}    http://${OC_ADDRESS}

${OC_MAINPAGE_ACCOUNT_SELECTOR}    //span[text()[contains(.,'My Account')]]
${OC_MAINPAGE_LOGIN_SELECTOR}    //a[text()[contains(.,'Login')]]
${OC_LOGIN_EMAIL_SELECTOR}    //*[@id="input-email"]
${OC_LOGIN_PASSWORD_SELECTOR}    //*[@id="input-password"]
${OC_LOGIN_LOGIN_BUTTON_SELECTOR}    //input[@value='Login']
${OC_LOGIN_TITLE_NEEDLE}    My Account
