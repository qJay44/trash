
Playspeed:=2 

Loop, 100
{

SetTitleMatchMode, 2
CoordMode, Mouse, Window

      tt = IdleWizard ahk_class UnityWndClass
      WinWait, %tt%
      IfWinNotActive, %tt%,, WinActivate, %tt%

  Sleep, % 407 //playspeed

MouseClick, L, 694, 965

MouseClick, L, 694, 965

  Sleep, % 422 //playspeed

MouseClick, L, 780, 967

  Sleep, % 313 //playspeed

MouseClick, L, 868, 962

  Sleep, 1000  //PlaySpeed 

}
