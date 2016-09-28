#!/bin/bash
# MAINTAINER Kinebas Kostiantyn, https://github.com/oookotooo, version 1.0
# This is script for automatic scene change for OBS linux, when you lock your screen
# First you need to setup hotkey (in this case Ctrl+1 and Ctrl+2) for changing
# scenes. After that instal xdotool to send keystrokes. Also here are
# some majic to send keystrokes directly to OBS.
###########################################################
### VARIABLES
###########################################################
# Your desktop environment interface, google a little bit
# to find out witch fit your linux. I use Ubuntu 14.04 with gnome DE
INTERFACE=org.gnome.ScreenSaver
# Process ID of OBS main window
OBSPID=`xdotool search --pid \`pidof obs\` 2>/dev/null | awk 'NR==4'`
###########################################################
### This script responsible for obs control
###########################################################
dbus-monitor --session "type='signal',interface='$INTERFACE'" |
  while read x; do
    case "$x" in 
      *"boolean true"*) 
      		xdotool key --window $OBSPID ctrl+2
      		echo -n "Заблокировано в " && date
      		;; #locked
      *"boolean false"*) 
      		xdotool key --window $OBSPID ctrl+1
      		echo -n "Разблокировано в " && date
      		;;  #unlocked
    esac
  done

# to test if it is found right OBS windows just run this command:
# xdotool key windowactivate `xdotool search --pid \`pidof obs\` 2>/dev/null | awk 'NR==4'`
