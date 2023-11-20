*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  tartsi  tartsi123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  tartsi  tartsi123
    Input  new
    Input Credentials  tartsi  tartsi123tartsi
    Output Should Contain  User with username tartsi already exists

Register With Too Short Username And Valid Password
    Input Credentials  t  tartsi123
    Output Should Contain  Username must be atleast 4 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  tartsi!  tartsi123
    Output Should Contain  Username must contain only letters from a-z

Register With Valid Username And Too Short Password
    Input Credentials  tartsi  t
    Output Should Contain  Password must be atleast 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  tartsi  tartsiiiiiiii
    Output Should Contain  Password cannot contain only letters

*** Keywords ***
Input New Command
    Input  new