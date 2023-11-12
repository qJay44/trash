
Playspeed:=2 

Loop, 1
{

SetTitleMatchMode, 2
CoordMode, Mouse, Window

      tt = Sven Co-op ahk_class SDL_app
      WinWait, %tt%
      IfWinNotActive, %tt%,, WinActivate, %tt%

  Sleep, % 844 //playspeed

MouseClick, R

  Sleep, % 890 //playspeed

MouseClick, R

  Sleep, % 1985 //playspeed

MouseClick, L

  Sleep, % 1078 //playspeed

Send, {Blind}r

  Sleep, % 1062 //playspeed


Loop, 9 {

	MouseClick, R

  	Sleep, % 500 //playspeed
}

MouseClick, L

  Sleep, % 700 //playspeed

Send, {Blind}r

  Sleep, 1000  //PlaySpeed 

}
