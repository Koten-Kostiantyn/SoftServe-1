; script will terminate your VPN connection (ShrewSoft)
WinSetState("VPN Connect","", @SW_RESTORE)
Send("{ENTER}")
WinClose("VPN Connect")
