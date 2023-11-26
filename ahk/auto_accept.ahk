#SingleInstance, Force
Hotkey, ^u, ToggeScript, T2

ToggeScript:
toggle := !toggle

WinGet, PID_Var, PID, ahk_exe Trove.exe

BackgroundClick(x, y, messageDelay, PID) {
	global toggle
	While, toggle {
		if %toggle% {
			lParam := x | (y << 16)

			SendMessage, 0x0006, 00000002, 00000000, , ahk_pid %PID% ;ACTIVE
			PostMessage, 0x0200, 00000001, %lParam%, , ahk_pid %PID% ;MOUSEMOVE

			Sleep, %messageDelay%
		}
    }
}

BackgroundClick(863, 473, 60000, PID_Var)
