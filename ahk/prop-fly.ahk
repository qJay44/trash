#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
;#Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

SetKeyDelay, 500

F3::
{
	Reload
}

#IfWinActive ahk_exe nmrih.exe
#MaxThreadsPerHotkey 2
XButton1::
{
	toggle := !toggle
	while (toggle and WinActive("ahk_exe nmrih.exe"))
	{
		Send, {space}
		Send, {e}
	}
}
