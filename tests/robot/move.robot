*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***         StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Valid Case #1              0             0             1                     NORTH         0           1           2
Invalid Case #2            0             0             5                     SOUTH         0           0           6
Valid Move #3              5             5             6                     NORTH         5           6
Valid Move #4              5             6             7                     SOUTH         5           5        
Valid Move #5              5             5             8                     EAST          6           5
Valid Move #6              6             5             9                     WEST          5           5
Invalid Move #7            1             9             15                    NORTH         1           9
Invalid Move #8            9             9             20                    EAST          9           9
Invalid Move #9            5             9             25                    NORTH         5           9
Invalid Move #10           9             5             30                    EAST          9           5 
Start Game #11                                                                             5           5    


*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}
