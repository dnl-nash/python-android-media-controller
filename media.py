from os import environ
from sys import argv as cmd
from subprocess import Popen
from shutil import which as findcmd
adb=findcmd("adb")
if(adb==None):
    print("Please install adb and place the binary in your path. The content of your path is: ",environ.get("PATH"))
    exit(2)
def play():
    Popen(args=[adb,"shell", "input keyevent MEDIA_PLAY_PAUSE"])
def rewind():
    Popen(args=[adb,"shell", "input keyevent MEDIA_REWIND"])
def fastforward():
    Popen(args=[adb,"shell", "input keyevent MEDIA_FAST_FORWARD"])
try:
    command=cmd[1]
except IndexError:
    print("Enter command, P play, R rewind, F fast forward.")
    command=input()
if(command=="p"):
    play()
elif(command=="r"):
    rewind()
elif(command=="f"):
    fastforward()
else:
    print("no valid command supplied.")
