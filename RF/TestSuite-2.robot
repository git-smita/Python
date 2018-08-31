*** Settings ***
Resource          Resource.robot

*** Variables ***
${BROWSER}        ${EMPTY}

*** Test Cases ***
Script-2
    Log    ${browser}
    Fail script    Script2 has failed.
