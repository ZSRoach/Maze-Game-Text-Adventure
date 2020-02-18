import entities
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



class Room:

    def __init__(self, layout):
        self.layout = layout
        self.south = None
        self.north = None
        self.east = None
        self.west = None
        self.eastEntrance = None
        self.westEntrance = None
        self.southEntrance = None
        self.northEntrance = None
        self.chestRoom = None
        self.tRE = None
        self.setDoorPositions()

    def setDoorSouth(self,adjacentRoom):
        self.south = adjacentRoom
        adjacentRoom.north = self

    def setDoorNorth(self,adjacentRoom):
        self.north = adjacentRoom
        adjacentRoom.south = self

    def setDoorEast(self,adjacentRoom):
        self.east = adjacentRoom
        adjacentRoom.west = self

    def setDoorWest(self,adjacentRoom):
        self.west = adjacentRoom
        adjacentRoom.east = self

    def setDoorPositions(self):
        for lineno, line in enumerate(self.layout):
            #check north doors:
            if lineno == 0:
                for i in range(len(line)):
                    space = line[i]
                    if space == "~":
                        self.northEntrance = [i,lineno+1]
            #check south doors
            if lineno == len(self.layout)-1:
                for i in range (len(line)):
                    space = line[i]
                    if space == "_":
                        self.southEntrance = [i,lineno-1]
            for i in range(len(line)):
                #check west doors
                space = line[i]
                if i == 0:
                    if space == "[":
                        self.westEntrance = [i+1,lineno]
                #check east doors
                if i == len(line)-1:
                    if space == "]":
                        self.eastEntrance = [i-1,lineno]


    def printRoom(self, playercoords):
        for lineno, line in enumerate(self.layout):
            playerline = line
            if playercoords[1] == lineno:
                playerline_parts = []
                for xval, char in enumerate(line):
                    if playercoords[0] == xval:
                        playerline_parts.append("P")
                    else:
                        playerline_parts.append(char)
                playerline = "".join(playerline_parts)
            print(colored(playerline, "white", attrs=["reverse"]))

    def roomSwitch(self, playercoords, tobeplayercoords, currentRoom):
        line_player_is_on = self.layout[tobeplayercoords[1]]
        space_player_is_on = line_player_is_on[tobeplayercoords[0]]
        if space_player_is_on == "~":
            return "north"
        if space_player_is_on == "[":
            return "west"
        if space_player_is_on == "]":
            return "east"
        if space_player_is_on == "_":
            return "south"
        return False

    def validMove(self, playercoords, tobeplayercoords):
        line_player_is_on = self.layout[tobeplayercoords[1]]
        space_player_is_on = line_player_is_on[tobeplayercoords[0]]
        if space_player_is_on == " ":
            return True
        return False

#All rooms go here:
#left of 2, below 8, above 9
startRoom = Room([
    "|--------------|",
    "|              |",
    "|              |",
    "|              ]",
    "|--------------|",
])
#right of 1, below 7, above 6, left of 3
room2 = Room([
    "|--------------|",
    "|              ]",
    "|          |   |",
    "[  |           |",
    "|--------------|",
])
#right of 2, above 4, below 5
room3 = Room([
    "|---------------~-|",
    "[    |            |",
    "| ---|    |       |",
    "|      |--|       |",
    "|      |          |",
    "|--------_--------|",
])
#below 3, above 10, right of 6
room4 = Room([
    "|--------~--------|",
    "|                 |",
    "|                 |",
    "|                 |",
    "|                 |",
    "|--------_--------|",
])
#TRE above 3, right of 7
room5 = Room([
    "|-----------------|",
    "|                 |",
    "|   |             |",
    "|           |     |",
    "[                 |",
    "|---------------_-|",
])
# above 11, right of 9, left of 4, below 2
room6 = Room([
    "|-----------------|",
    "|                 |",
    "[                 |",
    "|                 |",
    "|                 |",
    "|-----------------|",
])
#above 2, below 14, right of 8, left of 5
room7 = Room([
    "|-------------~---|",
    "|                 |",
    "|                 |",
    "|-----------------|",
    "|                 |",
    "[                 ]",
    "|-----------------|",
])
#left of 7, above start, below 13
room8 = Room([
    "|--------------~--|",
    "|                 |",
    "|                 |",
    "|    -------------|",
    "|                 |",
    "|                 ]",
    "|-----------------|",
])
#above 12, below start, left of 6
room9 = Room([
    "|-----------------|",
    "|                 |",
    "|                 ]",
    "|                 |",
    "|                 |",
    "|-_---------------|",
])
#below 4, right of 11
room10 = Room([
    "|--------~--------|",
    "|                 |",
    "|                 |",
    "|                 |",
    "[                 |",
    "|-----------------|",
])
#below 6, right of 12, left of 10
room11 = Room([
    "|-----------------|",
    "[                 |",
    "|                 |",
    "|                 |",
    "|                 ]",
    "|-----------------|",
])
#below 9, left of 11
room12 = Room([
    "|-~---------------|",
    "|                 ]",
    "|                 |",
    "|                 |",
    "|                 |",
    "|-----------------|",
])
#above 8, left of 14
room13 = Room([
    "|-----------------|",
    "|                 ]",
    "|                 |",
    "|                 |",
    "|--------------_--|",
])
#right of 13, above 7
room14 = Room([
    "|-----------------|",
    "[                 |",
    "|                 |",
    "|                 |",
    "|-------------_---|",
])

currentRoom = startRoom

startRoom.setDoorEast(room2)
room2.setDoorEast(room3)
room3.setDoorNorth(room5)
room3.setDoorSouth(room4)
room4.setDoorSouth(room10)
room10.setDoorWest(room11)
room11.setDoorWest(room12)
room12.setDoorNorth(room9)
room9.setDoorEast(room6)
room5.setDoorWest(room7)
room7.setDoorWest(room8)
room7.setDoorNorth(room14)
room13.setDoorSouth(room8)
room13.setDoorEast(room14)
gameRunning = True
player = Player()
player.fool(player)
while gameRunning:
    currentRoom.printRoom(playercoords)
    print (colored("\nAction Choices: \nW (up) \nA (left) \nS (down) \nD (right) \nE (interact - not implemented yet) \n", "white", attrs=["reverse"]))
    print (colored("Map Key: \n","white",attrs=["reverse"])+colored("P", "blue", "on_white")+colored(" - your character \n[ - door going west \n_ - door going south \n] - door going east \n~ - door going north \n---- or ||| - wall/block","white", attrs=["reverse"]))
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