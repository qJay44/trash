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
    Send, {a down}
    Sleep 15
    Send, {a up}
    Send, {d down}
    Sleep 15
    Send, {d up}
}
return

#IfWinActive Trove
!w::
Sleep, 100
Send, {w down}
return

