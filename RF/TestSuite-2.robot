*** Settings ***
Resource          Resource.robot

*** Variables ***
${browser}        FE

*** Test Cases ***
Script-2
    Log    ${browser}
    Fail script    Script2 has failed.
