#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


#MaxThreadsPerHotkey 2

#IfWinActive Trove
f5::
toggle := !toggle
Loop
{
    if not toggle
        break
    Click, Right

    Sleep, 60000
}
return

