
toggle = false

#MaxThreadsPerHotkey 2
#IfWinActive Trove
f5::
	toggle := !toggle

	While (toggle) {
		Send, {f}
		Sleep 11500
		Send, {f}
		Sleep 1000
	}
	
	Return
