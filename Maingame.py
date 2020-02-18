from Entities import Entity
from Entities import Player
from Entities import Sorcerer
from Entities import Rogue
from Entities import Warrior
from Entities import Necromancer
from Entities import Goblin
from rooms import Room
from rooms import startRoom
from rooms import room2
from rooms import room3
from rooms import room4
from rooms import room5
from rooms import room6
from rooms import room7
from rooms import room8
from rooms import room9
from rooms import room10
from rooms import room11
from rooms import room12
from rooms import room13
from rooms import room14
from rooms import room15
from rooms import room16
from rooms import room17
import random
import sys
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

currentRoom = startRoom


gameRunning = True
player = Sorcerer("Gamer")
player.fool(player)
while gameRunning:
    currentRoom.printRoom(playercoords)
    print (currentRoom.roomInfo)
    print (colored("\nAction Choices: \nW (up) \nA (left) \nS (down) \nD (right) \nE (interact - not implemented yet) \n", "white", attrs=["reverse"]))
    print (colored("Map Key: \n","white",attrs=["reverse"])+colored("Ö", "blue", "on_white")+colored(" - your character \n[ - door going west \n_ - door going south \n] - door going east \n~ - door going north \n---- or ||| - wall/block \n═ or ║ - locked door \n","white", attrs=["reverse"]))
    movement = getchar()
    if movement == "w":
        tobeplayercoords[1] -= 1

    if movement == "a":
        tobeplayercoords[0] -= 1

    if movement == "s":
        tobeplayercoords[1] += 1

    if movement == "d":
        tobeplayercoords[0] += 1
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
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
#hello this is a thing that i am doing