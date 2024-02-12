#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
;#Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

#IfWinActive ahk_pid 3632
#MaxThreadsPerHotkey 2
XButton1::
{
	toggle := !toggle
	While (toggle and WinActive("ahk_pid 3632"))
	{
		; Up-left
		MouseMove, 100, 100, 100
		Sleep, 500
		
		; Up-right
		MouseMove, 1820, 100
		Sleep, 500	
		
		; Middle-right
		MouseMove, 1820, 500
		Sleep, 500
		
		; Middle-left
		MouseMove, 100, 500
		Sleep, 500
				
		; Bottom-left
		MouseMove, 100, 1000
		Sleep, 500
		
		; Bottom-right
		MouseMove, 1820, 1000
		Sleep, 500
	}
	Return
}
