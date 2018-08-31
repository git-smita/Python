*** Settings ***
Resource          Resource.robot

*** Variables ***
${browser}        IE

*** Test Cases ***
Script-1
    Log    ${browser}
    Pass Script    Script1 has passed

*** Keywords ***
