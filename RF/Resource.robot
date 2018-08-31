*** Keywords ***
Pass Script
    [Arguments]    ${arg1}
    Pass Execution    ${arg1}

Fail Script
    [Arguments]    ${arg1}
    Fail    ${arg1}
