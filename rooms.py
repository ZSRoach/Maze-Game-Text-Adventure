import random
import sys
from copy import copy
import os
try:
  import termios
  import tty
except:
  import msvcrt


class Room:
  roomCount = []
  roomNames = []
  def __init__(self, roomName, layout, chestRoom, tRE, bossRoom, restRoom):
    self.layout = layout
    self.spawnedEnemies = False
    self.south = None
    self.north = None
    self.east = None
    self.west = None
    self.eastEntrance = None
    self.westEntrance = None
    self.southEntrance = None
    self.northEntrance = None
    self.roomName = roomName
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
    Room.roomCount.append(roomName)
    Room.roomNames.append(self)

  def roomInfoSave(self, saves, currentSaveFile):
    try:
      saves[currentSaveFile]["roomInfo"][self.roomName] = {}
    except KeyError as err:
      saves[currentSaveFile]["roomInfo"] = {}
      saves[currentSaveFile]["roomInfo"][self.roomName] = {}
    saves[currentSaveFile]["roomInfo"][self.roomName]["hasBeenVisited"] = self.hasBeenVisited
    try:
      saves[currentSaveFile]["roomInfo"][self.roomName]["locked"] = self.locked
    except AttributeError as err:
      worry = 1
    try:
      saves[currentSaveFile]["roomInfo"][self.roomName]["chestLooted"] = self.chestLooted
    except AttributeError as err:
      worry = 1
    try:
      saves[currentSaveFile]["roomInfo"][self.roomName]["spawnedEnemies"] = self.spawnedEnemies
    except AttributeError as err:
      worry = 1
  def roomSaveAll(saves, currentSaveFile):
    for roomNum, roomNameth in enumerate(Room.roomNames):
      roomNameth.roomInfoSave(saves, currentSaveFile)

  def roomInfoLoad(self, saves, currentSaveFile):
    self.hasBeenVisited = saves[currentSaveFile]["roomInfo"][self.roomName]["hasBeenVisited"]
    self.locked = saves[currentSaveFile]["roomInfo"][self.roomName]["locked"]
    self.chestLooted = saves[currentSaveFile]["roomInfo"][self.roomName]["chestLooted"]

  def roomLoadAll(saves, currentSaveFile):
    for roomNum, roomNameth in enumerate(Room.roomNames):
      roomNameth.roomInfoLoad(saves, currentSaveFile)

  def setChestLocation(self):
    for lineno, line in enumerate(self.layout):
      for i in range(len(line)):
        space = line[i]
        if space == "■":
          self.chestLocation = [i,lineno]

  def hasLockedDoor(self, lockedLayout, condition, player):
    self.lockedLayout = lockedLayout
    self.lockCondition = condition
    if self.lockCondition == True and player.isInteracting == True:
      self.locked = False
    elif self.lockCondition == True and self.locked != True:
      self.locked = False
    else:
      self.locked = True

  def lockConditionCheck(self, player):
      if self.lockCondition == True:
        self.locked = False

  def setRoomInfo(self, firstTime, secondTime):
    self.roomInfoFirst = firstTime
    self.roomInfoSecond = secondTime

  def displayRoomInfo(self):
    from Maingame import stdscr
    from Maingame import curses
    from Maingame import nextLine
    from Maingame import mapInfo
    if self.hasBeenVisited == True:
      nextLine()
      stdscr.addstr("Room Info:", curses.color_pair(1))
      try:
        nextLine()
        stdscr.addstr (self.roomInfoSecond, curses.color_pair(1))
      except AttributeError as err:
        nextLine()
        stdscr.addstr("There is no room info", curses.color_pair(1))
    else:
      nextLine()
      stdscr.addstr("Room Info:", curses.color_pair(1))
      try:
        nextLine()
        stdscr.addstr (self.roomInfoFirst, curses.color_pair(1))
      except AttributeError as err:
        nextLine()
        stdscr.addstr("There is no room info", curses.color_pair(1))

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
    from Maingame import stdscr
    from Maingame import curses
    from Maingame import nextLine
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
          nextLine()
          stdscr.addstr(playerline, curses.color_pair(1))
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
          nextLine()
          stdscr.addstr(playerline, curses.color_pair(1))

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

  def interactAction(self, playercoords, player, interactables, currentRoom, xpPerLevel):
    from Maingame import nextLine
    from Maingame import stdscr
    from Maingame import curses
    player.isInteracting = True
    line_player_is_on = self.layout[playercoords[1]]
    line_above_player = self.layout[playercoords[1]-1]
    line_below_player = self.layout[playercoords[1]+1]
    space_above_player = line_above_player[playercoords[0]]
    space_left_player = line_player_is_on[playercoords[0]-1]
    space_right_player = line_player_is_on[playercoords[0]+1]
    space_below_player = line_below_player[playercoords[0]]
    try:
      line_player_is_on_locked = self.lockedLayout[playercoords[1]]
      line_above_player_locked = self.lockedLayout[playercoords[1]-1]
      line_below_player_locked = self.lockedLayout[playercoords[1]+1]
      space_above_player_locked = line_above_player_locked[playercoords[0]]
      space_left_player_locked = line_player_is_on_locked[playercoords[0]-1]
      space_right_player_locked = line_player_is_on_locked[playercoords[0]+1]
      space_below_player_locked = line_below_player_locked[playercoords[0]]
    except AttributeError as err:
      space_above_player_locked = space_above_player
      space_left_player_locked = space_left_player
      space_right_player_locked = space_right_player
      space_below_player_locked = space_below_player

    for i in range (4):
      if i == 0:
        if space_above_player == "■":
          if currentRoom.chestLooted == True:
            nextLine()
            stdscr.addstr ("That chest has been looted already.", curses.color_pair(1))
          else:
            nextLine()
            stdscr.addstr ("You looted the chest above you", curses.color_pair(1))
            currentRoom.chestLoot(player, currentRoom, xpPerLevel)
        if space_above_player_locked == "═":
          currentRoom.lockConditionCheck(player)
          if currentRoom.locked == False:
            nextLine()
            stdscr.addstr ("You insert the key into the door above you and it unlocks.", curses.color_pair(1))
          else:
            nextLine()
            stdscr.addstr ("The door above you is locked. Maybe you can find a key somewhere...", curses.color_pair(1))
        if space_above_player == "☼":
          currentRoom.useHealingStation(player, currentRoom)

      if i == 1:
        if space_below_player == "■":
          if currentRoom.chestLooted == True:
            nextLine()
            stdscr.addstr ("That chest has been looted already.", curses.color_pair(1))
          else:
            nextLine()
            stdscr.addstr ("You looted the chest below you", curses.color_pair(1))
            currentRoom.chestLoot(player, currentRoom, xpPerLevel)
        if space_below_player_locked == "═":
          currentRoom.lockConditionCheck(player)
          if currentRoom.locked == False:
            nextLine()
            stdscr.addstr ("You insert the key into the door below you and it unlocks.", curses.color_pair(1))
          else:
            nextLine()
            stdscr.addstr ("The door below you is locked. Maybe you can find a key somewhere...", curses.color_pair(1))
        if space_below_player == "☼":
          currentRoom.useHealingStation(player, currentRoom)

      if i == 2:
        if space_left_player == "■":
          if currentRoom.chestLooted == True:
            nextLine()
            stdscr.addstr ("That chest has been looted already.", curses.color_pair(1))
          else:
            nextLine()
            stdscr.addstr ("You looted the chest to your left", curses.color_pair(1))
            currentRoom.chestLoot(player, currentRoom, xpPerLevel)
        if space_left_player_locked == "║":
          currentRoom.lockConditionCheck(player)
          if currentRoom.locked == False:
            nextLine()
            stdscr.addstr ("You insert the key into the door to your left and it unlocks.", curses.color_pair(1))
            currentRoom.locked = False
          else:
            nextLine()
            stdscr.addstr ("The door to your left is locked. Maybe you can find a key somewhere...", curses.color_pair(1))
        if space_left_player == "☼":
          currentRoom.useHealingStation(player, currentRoom)

      if i == 3:
        if space_right_player == "■":
          if currentRoom.chestLooted == True:
            nextLine()
            stdscr.addstr ("That chest has been looted already.", curses.color_pair(1))
          else:
            nextLine()
            stdscr.addstr ("You looted the chest to your right", curses.color_pair(1))
            currentRoom.chestLoot(player, currentRoom, xpPerLevel)
        if space_right_player_locked == "║":
          currentRoom.lockConditionCheck(player)
          if currentRoom.locked == False:
            nextLine()
            stdscr.addstr ("You insert the key into the door to your right and it unlocks.", curses.color_pair(1))
          else:
            nextLine()
            stdscr.addstr ("The door to your right is locked. Maybe you can find a key somewhere...", curses.color_pair(1))
        if space_right_player == "☼":
          currentRoom.useHealingStation(player, currentRoom)
    player.isInteracting = False

  def chestLoot(self, player, currentRoom, xpPerLevel):
    currentRoom.chestLooted = True
    if player.isSorcerer == 1:
      player.xp += (.2 * int(xpPerLevel[player.level - 1]))
    elif player.isWarrior == 1:
      player.xp += (.2 * int(xpPerLevel[player.level - 1]))
    elif player.isRogue == 1:
      player.xp += (.2 * int(xpPerLevel[player.level - 1]))
    else:
      player.xp += (.2 * int(xpPerLevel[player.level - 1]))

  def useHealingStation(self, player, currentRoom):
    from Maingame import stdscr
    from Maingame import curses
    from Maingame import nextLine
    nextLine()
    stdscr.addstr ("this is temporary holder", curses.color_pair(1))
    for roomNum, roomName in enumerate(Room.roomNames):
      roomName.spawnedEnemies = False

#═══════════ ║║║║║║║║║║║║║║║║║║║║
#All rooms go here:
#left of 2, below 8, above 9
startRoom = Room("startRoom", [
    "|--------------|",
    "|              |",
    "|       ☼      |",
    "|              ]",
    "|--------------|",
    ], False, False, False, True)
#right of 1, below 7, above 6, left of 3
room2 = Room("room2",[
    "|--------------|",
    "|              ]",
    "|          |   |",
    "[  |           |",
    "|-------_------|",
    ], False, False, False, False)
#right of 2, above 4, below 5
room3 = Room("room3",[
    "|---------------~-|",
    "[    |            |",
    "| ---|    |       |",
    "|      |--|       |",
    "|      |          |",
    "|--------_--------|",
    ], False, False, False, False)

#below 3, above 10, right of 6
room4 = Room("room4",[
    "|--------~--------|",
    "|                 |",
    "|                 |",
    "|                 |",
    "|                 |",
    "|--------_--------|",
    ], False, False, False, False)
#TRE above 3, right of 7
room5 = Room("room5",[
    "|-----------------|",
    "|                 |",
    "|   |             |",
    "|           |     |",
    "[                 |",
    "|---------------_-|",
    ], False, True, False, False)
# above 11, right of 9, left of 4, below 2
room6 = Room("room6",[
    "|--------~--------|",
    "|----|            |",
    "[    |   |-|----| |",
    "|    |   |■|----| |",
    "|        |        |",
    "|-----------------|",
    ], True, False, False, False)
#above 2, below 14, right of 8, left of 5
room7 = Room("room7",[
    "|-------------~---|",
    "|                 |",
    "|■                |",
    "|--------- -------|",
    "|                 |",
    "[                 ]",
    "|-----------------|",
    ], True, False, False, False)
#left of 7, above start, below 13
room8 = Room("room8",[
    "|--------------~--|",
    "|                 |",
    "|                 |",
    "|    -------------|",
    "|                 |",
    "|                 ]",
    "|-----------------|",
    ], False, False, False, False)
#above 12, below start, left of 6
room9 = Room("room9",[
    "|-----------------|",
    "|                 |",
    "|                 ]",
    "[                 |",
    "|                 |",
    "|-_---------------|",
    ], False, False, True, False)
#below 4, right of 11
room10 = Room("room10",[
    "|--------~--------|",
    "|                 |",
    "|                 |",
    "|                 |",
    "[                 |",
    "|-----------------|",
    ], False, False, False, False)
#below 6, right of 12, left of 10
room11 = Room("room11",[
    "|-----------------|",
    "[                 |",
    "|                 |",
    "|                 |",
    "|                 ]",
    "|-----------------|",
    ], False, False, False, False)
#below 9, left of 11
room12 = Room("room12",[
    "|-~---------------|",
    "|                 ]",
    "|                 |",
    "|                 |",
    "|                 |",
    "|-----------------|",
    ], False, False, False, False)
#above 8, left of 14
room13 = Room("room13",[
    "|-----------------|",
    "|                 ]",
    "|                 |",
    "|                 |",
    "|--------------_--|",
    ], False, False, False, False)
#right of 13, above 7
room14 = Room("room14",[
    "|-----------------|",
    "[                 |",
    "|                 |",
    "|                 |",
    "|-------------_---|",
    ], False, False, False, False)
#Left of 9, right of 16
room15 = Room("room15",[
    "|-----------------|",
    "[         |       |",
    "|                 |",
    "|         |       ]",
    "|         |       |",
    "|-----------------|",
    ], False, False, False, False)
#Left of 15, above 3-hall hallway
room16 = Room("room16",[
    "|-----------------|",
    "|                 ]",
    "|        |        |",
    "|               | |",
    "|                 |",
    "|---------_-------|",
    ], False, False, False, False)
#below 16
room17 = Room("room17",[
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
def conditionCheckAll(player):

  room3.hasLockedDoor([
    "|---------------~-|",
    "[    |            |",
    "| ---|    |       |",
    "|      |--|       |",
    "|      |          |",
    "|--------═--------|",
  ], room7.chestLooted, player)

  room7.hasLockedDoor([
    "|-------------~---|",
    "|                 |",
    "|■                |",
    "|---------═-------|",
    "|                 |",
    "[                 ]",
    "|-----------------|",
  ], room7.chestLooted, player)

  room2.hasLockedDoor([
    "|--------------|",
    "|              ]",
    "|          |   |",
    "[  |           |",
    "|-------═------|",
  ], room6.chestLooted, player)

  room6.hasLockedDoor([
    "|--------═--------|",
    "|----|            |",
    "[    |   |-|----| |",
    "|    |   |■|----| |",
    "|        |        |",
    "|-----------------|",
  ], room6.chestLooted, player)



#room info section
startRoom.setRoomInfo("You awake in a dark room. You see a small fire in the center, along with a door on the East wall.", "It's the room you first awoke in. The fire seems to still be burning. Maybe you should rest a while.")
room2.setRoomInfo("You travel to the next room, and see another door on the East wall and a locked door on the South wall. Where could it lead?", "Returning here, you feel the pull of the campfire drawing you to rest.")
room3.setRoomInfo("What","What?")
room4.setRoomInfo("Why","Why?!?")
room5.setRoomInfo("Who","WHO!")
room6.setRoomInfo("When","When!?!")
room7.setRoomInfo("Zach","Roach")
room8.setRoomInfo("spa", "ghet")
room9.setRoomInfo("Moving into this room, you feel the presence of a large creature.","It's the place you defeated the first boss, Turkey Panini. Returning, you feel as though there are others like him waiting for you deeper in the maze.")
room10.setRoomInfo("You notice the enemies getting stronger as you venture through the maze.","Returning, you wonder if the enemies are guiding you to the exit.")
room11.setRoomInfo("You feel a pull towards the northwest. It's as if something is waiting for you there.","Am I lost? I should've taken the shortcut.")
room12.setRoomInfo("You feel the pull to the North getting stronger. Something is in that next room.","Why have you returned to this room?")
room13.setRoomInfo("As you run into more enemies, you feel your power over the maze growing.","You now realize that there is still much to learn about your predicament")
room14.setRoomInfo("You feel something is pulling you to the South. It feels valuable to have.","Returning here, you ask yourself why you didn't take the shortcut to the South of the chest room.")

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
