#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
;#Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

SetKeyDelay, 500

#IfWinActive ahk_exe nmrih.exe
#MaxThreadsPerHotkey 2
*XButton1::
{
	toggle := !toggle
	Send, {Ctrl down}
	While (toggle and WinActive("ahk_exe nmrih.exe"))
	{
		Send, {Blind}{Space}
		Send, {Blind}{e}
	}
	Send, {Ctrl up}
	Return
}

#IfWinActive ahk_exe nmrih.exe
*Numpad6::
{
	Send, {Blind}{LShift down}
	Return	
}
