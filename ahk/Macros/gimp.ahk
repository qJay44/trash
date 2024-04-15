
Playspeed:=2 

Loop, 1
{

SetTitleMatchMode, 2
CoordMode, Mouse, Screen

      tt = *[v_fa_mac10_d-orig] (imported)-3.0 (RGB color 8-b ahk_class gdkWindowToplevel
      WinWait, %tt%
      IfWinNotActive, %tt%,, WinActivate, %tt%

  Sleep, % 687 //playspeed

Send, {Blind}{Ctrl Down}cv{Ctrl Up}

      tt = *[v_fa_mac10_d-orig] (imported)-3.0 (RGB color 8-b ahk_class gdkWindowToplevel
      WinWait, %tt%
      IfWinNotActive, %tt%,, WinActivate, %tt%

  Sleep, % 1266 //playspeed

MouseClick, L, 1656, 1022

  Sleep, % 1047 //playspeed

MouseClick, L, 1750, 1019

  Sleep, % 1422 //playspeed

MouseClick, L, 257, 36

  Sleep, % 1859 //playspeed

MouseClick, L, 320, 135

      tt = Hue-Saturation ahk_class gdkWindowToplevel
      WinWait, %tt%
      IfWinNotActive, %tt%,, WinActivate, %tt%

  Sleep, % 1312 //playspeed

MouseClick, L, 868, 487

MouseClick, L, 868, 487

MouseClick, L, 868, 487

MouseClick, L, 868, 486

MouseClick, L, 868, 486

MouseClick, L, 868, 486

MouseClick, L, 868, 486

MouseClick, L, 868, 486

  Sleep, % 235 //playspeed

MouseClick, L, 870, 486

MouseClick, L, 870, 486

  Sleep, % 1187 //playspeed

MouseClick, L, 755, 652

      tt = *[v_fa_mac10_d-orig] (imported)-3.0 (RGB color 8-b ahk_class gdkWindowToplevel
      WinWait, %tt%
      IfWinNotActive, %tt%,, WinActivate, %tt%

  Sleep, 1000  //PlaySpeed 

}
