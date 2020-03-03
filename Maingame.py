import curses
stdscr = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
import Entities
import rooms
import titlescreen
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

#player start position
playercoords = [1,1]
tobeplayercoords = [1,1]

currentRoom = rooms.startRoom


#Title Screen Loop - has start game button, load from save (experimental)

titleScreen = True
gameRunning = True
battling = False
cursorPos = 1

#erases screen before running
stdscr.refresh()

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

  elif titleMovement == "\r":
    if cursorPos == 1:
      titleScreen = False

  elif titleMovement == "\x1b":
    gameRunning = False
    titleScreen = False
    stdscr.erase()
    
  stdscr.erase()

#Character Creation Loop
player = Entities.Sorcerer("ZSRoach")
firstClear = 1
#Main Game Loop
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
    if currentRoom.hasBeenVisited:
      try:
        if len(currentRoom.roomInfoSecond) > len(max(mapInfo, key=len)):
          for i in range (len(currentRoom.roomInfoSecond)):
            stdscr.addstr(" ", curses.color_pair(1))
        else:
          for i in range (len(max(mapInfo, key=len))):
            stdscr.addstr(" ", curses.color_pair(1))
      except AttributeError as err:
        if len(roomInfoException) > len(max(mapInfo, key=len)):
          for i in range (len(roomInfoException)):
            stdscr.addstr(" ", curses.color_pair(1))
        else:
          for i in range (len(max(mapInfo, key=len))):
            stdscr.addstr(" ", curses.color_pair(1))
    else:
      try:
        if len(currentRoom.roomInfoFirst) > len(max(mapInfo, key=len)):
          for i in range (len(currentRoom.roomInfoFirst)):
            stdscr.addstr(" ", curses.color_pair(1))
        else:
          for i in range (len(max(mapInfo, key=len))):
            stdscr.addstr(" ", curses.color_pair(1))
      except AttributeError as err:
        if len(roomInfoException) > len(max(mapInfo, key=len)):
          for i in range (len(roomInfoException)):
            stdscr.addstr(" ", curses.color_pair(1))
        else:
          for i in range (len(max(mapInfo, key=len))):
            stdscr.addstr(" ", curses.color_pair(1))
    currentRoom.displayRoomInfo()
    for i in range (len(mapInfo)):
      nextLine()
      stdscr.addstr(mapInfo[i], curses.color_pair(1))
      try:
        if currentRoom.hasBeenVisited == True:
          if len(currentRoom.roomInfoSecond) > len(max(mapInfo, key=len)):
            spacesNeeded = len(currentRoom.roomInfoSecond)
          else:
            spacesNeeded = len(max(mapInfo, key=len))
        else:
          if len(currentRoom.roomInfoFirst) > len(max(mapInfo, key=len)):
            spacesNeeded = len(currentRoom.roomInfoFirst)
          else:
            spacesNeeded = len(max(mapInfo, key=len))
        spacesNeeded = spacesNeeded - len(mapInfo[i])
      except AttributeError as err:
        spacesNeeded = len(max(mapInfo, key=len))
        spacesNeeded = spacesNeeded - len(mapInfo[i])
      for i in range(spacesNeeded):
        stdscr.addstr(" ", curses.color_pair(1))
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
      try:
        if currentRoom.hasBeenVisited == True:
          spacesNeeded = len(currentRoom.roomInfoSecond)
        else:
          spacesNeeded = len(currentRoom.roomInfoFirst)
        spacesNeeded = spacesNeeded - len(updateString[i])
        for i in range(spacesNeeded):
          stdscr.addstr(" ", curses.color_pair(1))
      except AttributeError as err:
        spacesNeeded = len(max(mapInfo, key=len))
        spacesNeeded = spacesNeeded - len(updateString[i])
        for i in range (spacesNeeded):
          stdscr.addstr(" ",curses.color_pair(1))
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