import curses
stdscr = curses.initscr()
stdscr.clear()
curses.start_color()
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
stdscr.bkgd(" ", curses.color_pair(1))
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
import Entities
import rooms
import titlescreen
import savescreen
import charactermaking
import random
import sys
import json
from copy import copy
import os
try:
  import termios
  import tty
except:
  import msvcrt

with open("saves", "r") as reading:
  try:
    saves = json.loads(reading.read())
  except json.decoder.JSONDecodeError as err:
    saves = []
    saves.insert(0,{
      "Used": False,
    })
    saves.insert(1,{
      "Used": False,
    })
    saves.insert(2,{
      "Used": False,
    })


def nextLine():
  pos = stdscr.getyx()
  ypos = pos[0]
  xpos= pos[1]
  stdscr.move(ypos+1,0)
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




#Title Screen Loop - has start game button, load from save (experimental)

titleScreen = True
newScreen = False
loadScreen = False
characterMakingScreen = False
gameRunning = True
battling = False
cursorPos = 1

#erases screen before running
stdscr.refresh()
while titleScreen or newScreen or loadScreen or characterMakingScreen:
  #Main Title Screen Loop
  while titleScreen:
    titlescreen.printTitleScreen(cursorPos)
    stdscr.refresh()
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

    #when enter is pressed
    elif titleMovement == "\r":
      if cursorPos == 1:
        titleScreen = False
        loadScreen = False
        newScreen = True
      elif cursorPos == 2:
        titleScreen = False
        newScreen = False
        loadScreen = True

    elif titleMovement == "\x1b":
      gameRunning = False
      titleScreen = False
      newScreen = False
      loadScreen = False
      stdscr.erase()
      
    stdscr.erase()

  #Character New File Loop
  stdscr.refresh()
  cursorPos = 1
  while newScreen:
    savescreen.printNewScreen(cursorPos)
    stdscr.refresh()
    newMovement = getchar()
    if newMovement == "w":
      if cursorPos == 1 or cursorPos == 2 or cursorPos == 3:
        cursorPos == 4
      else:
        cursorPos = 2

    elif newMovement == "s":
      if cursorPos == 1 or cursorPos == 2 or cursorPos == 3:
        cursorPos = 4
      else:
        cursorPos = 2

    elif newMovement == "a":
      if cursorPos == 1:
        cursorPos = 3
      elif cursorPos == 2:
        cursorPos = 1
      elif cursorPos == 3:
        cursorPos = 2
      elif cursorPos == 4:
        cursorPos = 1

    elif newMovement == "d":
      if cursorPos == 1:
        cursorPos = 2
      elif cursorPos == 2:
        cursorPos = 3
      elif cursorPos == 3:
        cursorPos = 1
      elif cursorPos == 4:
        cursorPos = 3

    #if enter is pressed
    elif newMovement == "\r":
      if cursorPos == 1:
        if saves[0]["Used"] == False:
          currentSaveFile = 0
          saves[0]["Used"] = True
          nextLine()
          stdscr.addstr("You have selected file 1", curses.color_pair(1))
          newScreen = False
          characterMakingScreen = True
        else:
          nextLine()
          stdscr.addstr("That file already has a save in it", curses.color_pair(1))

      elif cursorPos == 2:
        if saves[1]["Used"] == False:
          currentSaveFile = 1
          saves[1]["Used"] = True
          nextLine()
          stdscr.addstr("You have selected file 2", curses.color_pair(2))
        else:
          nextLine()
          stdscr.addstr("That file already has a save in it", curses.color_pair(1))

      elif cursorPos == 3:
        if saves[2]["Used"] == False:
          currentSaveFile = 2
          saves[2]["Used"] = True
          nextLine()
          stdscr.addstr("You have selected file 3", curses.color_pair(2))
        else:
          nextLine()
          stdscr.addstr("That file already has a save in it", curses.color_pair(1))

      elif cursorPos == 4:
        titleScreen = True
        newScreen = False
        loadScreen = False

    elif newMovement == "\x1b":
      gameRunning = False
      titleScreen = False
      newScreen = False
      loadScreen = False
      stdscr.erase()
      
    stdscr.erase()

  while characterMakingScreen:


  while loadScreen:
    buh

player = Entities.Sorcerer("ZSRoach")

#player start position
playercoords = [1,1]
tobeplayercoords = [1,1]
currentRoom = rooms.startRoom

#Main Game Loop
firstClear = 1
interactables = 4
while gameRunning == True or battling == True:
  while gameRunning:
    mapInfo = [" ",
    "Action Choices:",
    "W (up)",
    "A (left)",
    "S (down)",
    "D (right)",
    "E (interact)",
    " ",
    "Map Key:",
    "Ö - your character",
    "[ - door going west",
    "_ - door going south",
    "] - door going east",
    "~ - door going north",
    "---- or ||| - wall/block",
    "■ - chest",
    "δ - enemy",
    "Ω - boss",
    ]
    roomInfoException = "There is no room info"
    rooms.conditionCheckAll(player)
    currentRoom.printRoom(playercoords)
    nextLine()
    currentRoom.displayRoomInfo()
    for i in range (len(mapInfo)):
      nextLine()
      stdscr.addstr(mapInfo[i], curses.color_pair(1))
    stdscr.refresh()
    currentRoom.hasBeenVisited = True
    action = getchar()
    stdscr.erase()
    if firstClear == 1:
      stdscr.clear()
      firstClear = 0
    updateString = ["Updates:",
    "",
    ]
    for i in range (len(updateString)):
      if i != 0:
        nextLine()
      stdscr.addstr(updateString[i], curses.color_pair(1))
    nextLine()
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
  
  while battling:
    stdscr.addstr("Battling")



curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()