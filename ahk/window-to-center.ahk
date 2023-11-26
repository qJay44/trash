^y::
  WinGetTitle, ActiveWindowTitle, A
  WinGetPos,,, Width, Height, %ActiveWindowTitle%
  TargetX := (A_ScreenWidth / 2) - (Width / 2)
  TargetY := (A_ScreenHeight / 2) - (Height / 2)
  WinMove, %ActiveWindowTitle%,, %TargetX%, %TargetY%
  Return

