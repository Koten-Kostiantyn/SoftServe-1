#cs ----------------------------------------------------------------------------
 AutoIt Version: 3.3.12.0
 Author:         Kostiantyn Kinebas
 Script Function:
	Fast connect to cisco VPN(shrew soft).
#ce ----------------------------------------------------------------------------
; It is configured for Windows 7(Should be ok on 10), and 1920*1080 screen resolution.
; Also place SofTokenII window in bottom-right corner of your desktop.
; If you have multiple monitors, script is configured for using main screen.
; To reconfigure this script use AutoIt window info and find fields in comment sections.
Func SofTokenII(); acquire token
    Local $iPID = Run("C:\Program Files (x86)\Secure Computing\SofToken-II\SofToken-II.exe", "", @SW_SHOWMAXIMIZED); syspath to SofToken II app
	mousemove(158, 192)
	WinWait("SofToken II")
    mouseclick("left",158, 192); by default you should choose user, this is place for "OK" button
    mousemove(1824, 908)
	WinWait("SofToken II")
	mouseclick("left",1824, 908); now it is our softokenII window in left bottom corner, click on PIN field
	Send("%%%YOUR PIN%%%"); input your PIN
	mouseclick("left",1676, 959); click "get password"
	mouseclick("left",1826, 956, 2); double click on newly generated password
	Send("^c") ; copy to clip
	mouseclick("left",1831, 1010); click "Close"
    ProcessClose($iPID) ; end process
EndFunc
Func ShrewSoft(); connect to VPN using shrew soft app. (uncomment any section you need to click on it)
    Local $iPID = Run("C:\Program Files\ShrewSoft\VPN Client\ipseca.exe", "", @SW_SHOWMAXIMIZED); syspath to ShrewSoft app
	   mousemove(38, 115)
	   WinWait("VPN Access Manager")
	   mouseclick("left",38, 115, 2); double click to connect to 1st server in list (use large icons)
	   #cs ----------------------------------------------------------------------------
	   mousemove(113, 115)
	   WinWait("VPN Access Manager")
	   mouseclick("left",113, 115, 2); double click to connect to 2nd server in list (use large icons)
	   mousemove(188, 115)
	   WinWait("VPN Access Manager")
	   mouseclick("left",188, 115, 2); double click to connect to 3rd server in list (use large icons)
	   mousemove(264, 115)
	   WinWait("VPN Access Manager")
	   mouseclick("left",264, 115, 2); double click to connect to 4th server in list (use large icons)
	   #ce ----------------------------------------------------------------------------
	mousemove(954, 627)
	WinWait("VPN Connect")
	Send("^v"); insert token from clipboard
	mouseclick("left",954, 627);
	mousemove(1117, 601)
	WinWait("VPN Gateway Login Banner")
	mouseclick("left",1117, 601);
    ProcessClose($iPID) ; end process
EndFunc

SofTokenII();
ShrewSoft();
