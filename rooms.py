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

class Room:
  def __init__(self, layout, chestRoom, tRE, bossRoom, restRoom):
    self.layout = layout
    self.south = None
    self.north = None
    self.east = None
    self.west = None
    self.eastEntrance = None
    self.westEntrance = None
    self.southEntrance = None
    self.northEntrance = None
    self.chestRoom = chestRoom
    self.tRE = tRE
    self.bossRoom = bossRoom
    self.restRoom = restRoom
    self.setDoorPositions()
    self.hasBeenVisited = False
    self.locked = False
    self.lockCondition = None
    self.chestLooted = False
    self.chestLocation = None
    self.setChestLocation()

    
  def setChestLocation(self):
      for lineno, line in enumerate(self.layout):
        for i in range(len(line)):
          space = line[i]
          if space == "■":
            self.chestLocation = [i,lineno]

  def hasLockedDoor(self, lockedLayout, condition):
      self.lockedLayout = lockedLayout
      self.locked = True
      self.lockCondition = condition
      
  def lockConditionCheck(self):
      if self.lockCondition == True:
        self.locked = False

  def setRoomInfo(self, firstTime, secondTime):
      print ("hi")

  def displayRoomInfo(self):
      print ("hi")

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
    if self.locked == True:
      for lineno, line in enumerate(self.lockedLayout):
          playerline = line
          if playercoords[1] == lineno:
              playerline_parts = []
              for xval, char in enumerate(line):
                  if playercoords[0] == xval:
                      playerline_parts.append("Ö")
                  else:
                      playerline_parts.append(char)
              playerline = "".join(playerline_parts)
          print(colored(playerline, "white", attrs=["reverse"]))
    else:
      for lineno, line in enumerate(self.layout):
          playerline = line
          if playercoords[1] == lineno:
              playerline_parts = []
              for xval, char in enumerate(line):
                  if playercoords[0] == xval:
                      playerline_parts.append("Ö")
                  else:
                      playerline_parts.append(char)
              playerline = "".join(playerline_parts)
          print(colored(playerline, "white", attrs=["reverse"]))

  def roomSwitch(self, playercoords, tobeplayercoords, currentRoom):
    if self.locked == True:
      line_player_is_on = self.lockedLayout[tobeplayercoords[1]]
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
    else:
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
    if self.locked == True:
      line_player_is_on = self.lockedLayout[tobeplayercoords[1]]
      space_player_is_on = line_player_is_on[tobeplayercoords[0]]
      if space_player_is_on == " ":
          return True
      return False
    else:
      line_player_is_on = self.layout[tobeplayercoords[1]]
      space_player_is_on = line_player_is_on[tobeplayercoords[0]]
      if space_player_is_on == " ":
          return True
      return False
  
  def interactAction(self, playercoords, player, interactables, currentRoom):
    player.isInteracting = True
    for lineno, line in enumerate(self.layout):
      line_player_is_on = self.layout[playercoords[1]]
      line_above_player = self.layout[playercoords[1]-1]
      line_below_player = self.layout[playercoords[1]+1]
      space_above_player = line_above_player[playercoords[0]]
      space_left_player = line_player_is_on[playercoords[0]-1]
      space_right_player = line_player_is_on[playercoords[0]+1]
      space_below_player = line_below_player[playercoords[0]]
      for i in range (4):
        for x in range(interactables):
          if i == 0:
            
    player.isInteracting = False
      
  def chestLoot(self, player, currentRoom):
    currentRoom.chestLooted = True
    if player.isSorcerer == 1:
      player.xp += (.2 * Entities.xpPerLevel[player.level])
    elif player.isWarrior == 1:
      player.xp += (.2 * Entities.xpPerLevel[player.level])
    elif player.isRogue == 1:
      player.xp += (.2 * Entities.xpPerLevel[player.level])
    else:
      player.xp += (.2 * Entities.xpPerLevel[player.level])

#All rooms go here:
#left of 2, below 8, above 9
startRoom = Room([
    "|--------------|",
    "|              |",
    "|              |",
    "|              ]",
    "|--------------|",
    ], False, False, False, True)
#right of 1, below 7, above 6, left of 3
room2 = Room([
    "|--------------|",
    "|              ]",
    "|          |   |",
    "[  |           |",
    "|-------_------|",
    ], False, False, False, False)
#right of 2, above 4, below 5
room3 = Room([
    "|---------------~-|",
    "[    |            |",
    "| ---|    |       |",
    "|      |--|       |",
    "|      |          |",
    "|--------_--------|",
    ], False, False, False, False)

#below 3, above 10, right of 6
room4 = Room([
    "|--------~--------|",
    "|                 |",
    "|                 |",
    "|                 |",
    "|                 |",
    "|--------_--------|",
    ], False, False, False, False)
#TRE above 3, right of 7
room5 = Room([
    "|-----------------|",
    "|                 |",
    "|   |             |",
    "|           |     |",
    "[                 |",
    "|---------------_-|",
    ], False, True, False, False)
# above 11, right of 9, left of 4, below 2
room6 = Room([
    "|--------~--------|",
    "|                 |",
    "[                 |",
    "|                 |",
    "|                 |",
    "|-----------------|",
    ], True, False, False, False)
#above 2, below 14, right of 8, left of 5
room7 = Room([
    "|-------------~---|",
    "|                 |",
    "|■                |",
    "|--------- -------|",
    "|                 |",
    "[                 ]",
    "|-----------------|",
    ], True, False, False, False)
#left of 7, above start, below 13
room8 = Room([
    "|--------------~--|",
    "|                 |",
    "|                 |",
    "|    -------------|",
    "|                 |",
    "|                 ]",
    "|-----------------|",
    ], False, False, False, False)
#above 12, below start, left of 6
room9 = Room([
    "|-----------------|",
    "|                 |",
    "|                 ]",
    "[                 |",
    "|                 |",
    "|-_---------------|",
    ], False, False, True, False)
#below 4, right of 11
room10 = Room([
    "|--------~--------|",
    "|                 |",
    "|                 |",
    "|                 |",
    "[                 |",
    "|-----------------|",
    ], False, False, False, False)
#below 6, right of 12, left of 10
room11 = Room([
    "|-----------------|",
    "[                 |",
    "|                 |",
    "|                 |",
    "|                 ]",
    "|-----------------|",
    ], False, False, False, False)
#below 9, left of 11
room12 = Room([
    "|-~---------------|",
    "|                 ]",
    "|                 |",
    "|                 |",
    "|                 |",
    "|-----------------|",
    ], False, False, False, False)
#above 8, left of 14
room13 = Room([
    "|-----------------|",
    "|                 ]",
    "|                 |",
    "|                 |",
    "|--------------_--|",
    ], False, False, False, False)
#right of 13, above 7
room14 = Room([
    "|-----------------|",
    "[                 |",
    "|                 |",
    "|                 |",
    "|-------------_---|",
    ], False, False, False, False)
#Left of 9, right of 16
room15 = Room([
    "|-----------------|",
    "[         |       |",
    "|                 |",
    "|         |       ]",
    "|         |       |",
    "|-----------------|",
    ], False, False, False, False)
#Left of 15, above 3-hall hallway
room16 = Room([
    "|-----------------|",
    "|                 ]",
    "|        |        |",
    "|               | |",
    "|                 |",
    "|---------_-------|",
    ], False, False, False, False)
#below 16
room17 = Room([
    "|---------~----------|",
    "|     |        |     |",
    "|     |        |     |",
    "|     |        |     |",
    "|     |        |     |",
    "|     |        |     |",
    "|     |        |     |",
    "|     |        |     |",
    "|---------_----------|",
    ], True, False, False, False)

# ════════════════════════        ║║║║║║║║║║║║║║║║║║║║
#doors with locks:
def conditionCheckAll():

  room3.hasLockedDoor([
    "|---------------~-|",
    "[    |            |",
    "| ---|    |       |",
    "|      |--|       |",
    "|      |          |",
    "|--------═--------|",
  ], room7.chestLooted)

  room7.hasLockedDoor([
    "|-------------~---|",
    "|                 |",
    "|■                |",
    "|---------═-------|",
    "|                 |",
    "[                 ]",
    "|-----------------|",
  ], room7.chestLooted)





#Door declarations:
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
room9.setDoorWest(room15)
room16.setDoorEast(room15)
room16.setDoorSouth(room17)
room6.setDoorNorth(room2)