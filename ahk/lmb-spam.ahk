F9::
{
	Send, {Ctrl down}
	Loop, 50
	{
		Send, {LButton down}
		Sleep, 10
		Send, {LButton up}
	}
	Send, {Ctrl up}
	Return
}
