import Entities
import rooms
import titlescreen
import random
import sys
import json
from copy import copy
import os
from termcolor import colored
try:
  import termios
  import tty
except:
  import msvcrt

#uses old 1970"s programming crap to not buffer inputs from keyboard
def getchar():
  if sys.platform == "win32":
    return msvcrt.getch().decode("utf-8")
  else:
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
      tty.setraw(fd)
      ch = sys.stdin.read(1)
    finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

#player start position
playercoords = [1,1]
tobeplayercoords = [1,1]

currentRoom = rooms.startRoom


    #Title Screen Loop - has start game button, load from save (experimental)

titleScreen = True
gameRunning = True
cursorPos = 1

#clears screen before running
if sys.platform == "win32":
  os.system("cls")
else:
  os.system("clear")

while titleScreen:
  titlescreen.printTitleScreen(cursorPos)
  titleMovement = getchar()
  if titleMovement == "w":
    if cursorPos == 1:
      cursorPos = 2
    else:
     cursorPos = 1

  elif titleMovement == "s":
    if cursorPos == 1:
      cursorPos = 2
    else:
      cursorPos = 1

  elif titleMovement == "\r":
    if cursorPos == 1:
      titleScreen = False

  elif titleMovement == "\x1b":
    gameRunning = False
    titleScreen = False
    print ()
  if sys.platform == "win32":
    os.system("cls")
  else:
    os.system("clear")

#Character Creation Loop
player = Entities.Sorcerer("ZSRoach")

#Main Game Loop
interactables = 4

while gameRunning:
  print("")
  rooms.conditionCheckAll(player)
  currentRoom.printRoom(playercoords)
  currentRoom.displayRoomInfo()
  currentRoom.hasBeenVisited = True
  print (colored("\n Action Choices: \n W (up) \n A (left) \n S (down) \n D (right) \n E (interact) \n", "white", attrs=["reverse"]))
  print (colored(" Map Key: \n ","white",attrs=["reverse"])+colored("Ö", "blue", "on_white")+colored(" - your character \n [ - door going west \n _ - door going south \n ] - door going east \n ~ - door going north \n ---- or ||| - wall/block \n ═ or ║ - locked door \n ■ - chest \n δ - enemy \n Ω - boss","white", attrs=["reverse"]))
  action = getchar()
  if sys.platform == "win32":
    os.system("cls")
  else:
    os.system("clear")
  print(colored("Updates:\n----------------------------------------------------","white",attrs=["reverse"]))
  if action == "w":
    tobeplayercoords[1] -= 1

  if action == "a":
    tobeplayercoords[0] -= 1

  if action == "s":
    tobeplayercoords[1] += 1

  if action == "d":
    tobeplayercoords[0] += 1

  if action == "e":
    currentRoom.interactAction(playercoords, player, interactables, currentRoom, Entities.xpPerLevel)

  if action == "\x1b":
    gameRunning = False
    break

  if currentRoom.roomSwitch(playercoords,tobeplayercoords,currentRoom) == "north":
    currentRoom = currentRoom.north
    tobeplayercoords = copy(currentRoom.southEntrance)
    playercoords = copy(tobeplayercoords)
  elif currentRoom.roomSwitch(playercoords,tobeplayercoords,currentRoom) == "south":
    currentRoom = currentRoom.south
    tobeplayercoords = copy(currentRoom.northEntrance)
    playercoords = copy(tobeplayercoords)
  elif currentRoom.roomSwitch(playercoords,tobeplayercoords,currentRoom) == "east":
    currentRoom = currentRoom.east
    tobeplayercoords = copy(currentRoom.westEntrance)
    playercoords = copy(tobeplayercoords)
  elif currentRoom.roomSwitch(playercoords,tobeplayercoords,currentRoom) == "west":
    currentRoom = currentRoom.west
    tobeplayercoords = copy(currentRoom.eastEntrance)
    playercoords = copy(tobeplayercoords)
  elif currentRoom.validMove(playercoords,tobeplayercoords):
    playercoords = copy(tobeplayercoords)
  else:
    tobeplayercoords = copy(playercoords)
#hello this is a thing that i am doing
