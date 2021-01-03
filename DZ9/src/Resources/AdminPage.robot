*** Settings ***
Resource  Variables.robot

*** Variables ***
${ADMINNAME}    demo
${ADMINPASSWORD}    demo
${OC_ADMINPAGE}    http://${OC_ADDRESS}/admin/

${OC_ADMINPAGE_USERNAME_SELECTOR}    //input[@placeholder='Username']
${OC_ADMINPAGE_PASSWORD_SELECTOR}    //input[@placeholder='Password']
${OC_ADMINPAGE_LOGIN_BUTTON_SELECTOR}    //button[text()[contains(.,'Login')]]
${OC_ADMINPAGE_TITLE_NEEDLE}    Dashboard
