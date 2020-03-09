import curses
stdscr = curses.initscr()
stdscr.clear()
curses.start_color()
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
stdscr.bkgd(" ", curses.color_pair(1))
curses.noecho()
stdscr.keypad(True)
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

if __name__ == "__main__":
  loadedFile = 0
  import Entities
  import rooms
  import titlescreen
  import savescreen
  import charactermaking

  def playerSet(saves, currentSaveFile):
    try:
      if saves[currentSaveFile]["Sorcerer"] == True:
        return Entities.Sorcerer(saves[currentSaveFile]["Name"])
      if saves[currentSaveFile]["Warrior"] == True:
        return Entities.Warrior(saves[currentSaveFile]["Name"])
      if saves[currentSaveFile]["Rogue"] == True:
        return Entities.Rogue(saves[currentSaveFile]["Name"])
      if saves[currentSaveFile]["Necromancer"] == True:
        return Entities.Necromancer(saves[currentSaveFile]["Name"])
    except:
      worry = 1
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

  def checkName(saves, currentSaveFile):
    import rooms
    for i in range (len(rooms.Room.roomCount)):
      if saves[currentSaveFile]["currentRoomName"] == rooms.Room.roomCount[i]:
        toBeCurrentRoom = rooms.Room.roomCount[i]
        return toBeCurrentRoom
      
  def setCurrentRoom(toBeRoom):
    if toBeRoom == rooms.Room.roomCount[0]:
      currentRoom = rooms.startRoom
      return currentRoom
    if toBeRoom == rooms.Room.roomCount[1]:
      currentRoom = rooms.room2
      return currentRoom
  
  def saveInfo(player, currentRoom, saves, saveFile):
    try:
      saves[saveFile]["currentRoomName"] = currentRoom.name
    except AttributeError as err:
      worry = 1
    try:
      if player.isSorcerer == 1:
        saves[saveFile]["Sorcerer"] = True
    except AttributeError as err:
      worry = 1
    try:
      if player.isWarrior == 1:
        saves[saveFile]["Warrior"] = True
    except AttributeError as err:
      worry = 1
    try:
      if player.isNecromancer == 1:
        saves[saveFile]["Necromancer"] = True
    except AttributeError as err:
      worry = 1
    try:
      if player.isRogue == 1:
        saves[saveFile]["Rogue"] = True
    except AttributeError as err:
      worry = 1
    try:
      saves[saveFile]["XP"] = player.xp
    except AttributeError as err:
      worry = 1
    try:
      saves[saveFile]["Health"] = player.health
    except AttributeError as err:
      worry = 1
    try:
      saves[saveFile]["Attack"] = player.attack
    except AttributeError as err:
      worry = 1
    try:
      saves[saveFile]["Defense"] = player.defense
    except AttributeError as err:
      worry = 1
    try:
      saves[saveFile]["Speed"] = player.speed
    except AttributeError as err:
      worry = 1
    try:
      saves[saveFile]["Name"] = player.name
    except AttributeError as err:
      worry = 1
    try:
      saves[saveFile]["Mana"] = player.mana
    except AttributeError as err:
      worry = 1
    try:
      saves[saveFile]["Spells"] = player.spells
    except AttributeError as err:
      worry = 1
    try:
      saves[saveFile]["ManaRegen"] = player.manaRegen
    except AttributeError as err:
      worry = 1
    try:
      saves[saveFile]["SpellDamage"] = player.spellDamage
    except AttributeError as err:
      worry = 1
    try:
      saves[saveFile]["TwoHanded"] = player.twoHanded
    except AttributeError as err:
      worry = 1
    try:
      saves[saveFile]["EvadeChance"] = player.evadeChance
    except AttributeError as err:
      worry = 1
    try:
      saves[saveFile]["Stealth"] = player.stealth
    except AttributeError as err:
      worry = 1
    try:
      saves[saveFile]["MaxMinions"] = player.maxMinions
    except AttributeError as err:
      worry = 1
    try:
      saves[saveFile]["MinionsAlive"] = player.currentMinionsAlive
    except AttributeError as err:
      worry = 1
    try:
      saves[saveFile]["CurrentMinionCount"] = player.currentMinions
    except AttributeError as err:
      worry = 1
    try:
      saves[saveFile]["MinionHealth"] = player.minionHealth
    except AttributeError as err:
      worry = 1
    try:
      saves[saveFile]["MinionAttack"] = player.minionAttack
    except AttributeError as err:
      worry = 1

  #Title Screen Loop - has start game button, load from save (experimental)

  titleScreen = True
  newScreen = False
  loadScreen = False
  gameRunning = True
  battling = False
  cursorPos = 1
  #erases screen before running
  stdscr.refresh()
  while titleScreen or newScreen or loadScreen:
    #Main Title Screen Loop
    cursorPos = 1
    while titleScreen == True:
      nextLine()
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
          loadScreen = False
          newScreen = True
          titleScreen = False
        elif cursorPos == 2:
          newScreen = False
          loadScreen = True
          titleScreen = False

      elif titleMovement == "\x1b":
        gameRunning = False
        titleScreen = False
        newScreen = False
        loadScreen = False
        stdscr.erase()
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        break
      stdscr.erase()

    #Character New File Loop
    stdscr.refresh()
    cursorPos = 1
    while newScreen:
      nextLine()
      savescreen.printNewScreen(cursorPos)
      stdscr.refresh()
      newMovement = getchar()
      stdscr.erase()
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
            player = charactermaking.classChoice()
            newScreen = False
          else:
            nextLine()
            stdscr.addstr("That file already has a save in it", curses.color_pair(1))

        elif cursorPos == 2:
          if saves[1]["Used"] == False:
            currentSaveFile = 1
            saves[1]["Used"] = True
            nextLine()
            stdscr.addstr("You have selected file 2", curses.color_pair(1))
            player = charactermaking.classChoice()
            newScreen = False
          else:
            nextLine()
            stdscr.addstr("That file already has a save in it", curses.color_pair(1))

        elif cursorPos == 3:
          if saves[2]["Used"] == False:
            currentSaveFile = 2
            saves[2]["Used"] = True
            nextLine()
            stdscr.addstr("You have selected file 3", curses.color_pair(1))
            player = charactermaking.classChoice()
            newScreen = False
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
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        break   
    
    stdscr.refresh()
    cursorPos = 1
    while loadScreen:
      nextLine()
      savescreen.printLoadScreen(cursorPos)
      stdscr.refresh()
      loadMovement = getchar()
      stdscr.erase()
      if loadMovement == "w": 
        if cursorPos == 1 or cursorPos == 2:
          cursorPos = 5
        elif cursorPos == 3:
          cursorPos = 4
        elif cursorPos == 4:
          cursorPos = 3
        elif cursorPos == 5:
          cursorPos = 1

      elif loadMovement == "s":
        if cursorPos == 1 or cursorPos == 2:
          cursorPos = 5
        elif cursorPos == 3:
          cursorPos = 4
        elif cursorPos == 4:
          cursorPos = 3
        elif cursorPos == 5:
          cursorPos = 1

      elif loadMovement == "a":
        if cursorPos == 1:
          cursorPos = 3
        elif cursorPos == 2:
          cursorPos = 1
        elif cursorPos == 3:
          cursorPos = 2
        elif cursorPos == 4:
          cursorPos = 5
        elif cursorPos == 5:
          cursorPos = 4

      elif loadMovement == "d":
        if cursorPos == 1:
          cursorPos = 2
        elif cursorPos == 2:
          cursorPos = 3
        elif cursorPos == 3:
          cursorPos = 1
        elif cursorPos == 4:
          cursorPos = 5
        elif cursorPos == 5:
          cursorPos = 4
      
      #if enter is pressed
      elif loadMovement == "\r":
        if cursorPos == 1:
          if saves[0]["Used"] == True:
            currentSaveFile = 0
            nextLine()
            stdscr.addstr("You have selected file 1", curses.color_pair(1))
            player = playerSet(saves, currentSaveFile)
            rooms.Room.roomLoadAll(saves, currentSaveFile)
            loadedFile = 1
            loadScreen = False
          else:
            nextLine()
            stdscr.addstr("That file does not have a save in it", curses.color_pair(1))

        elif cursorPos == 2:
          if saves[1]["Used"] == True:
            currentSaveFile = 1
            nextLine()
            stdscr.addstr("You have selected file 2", curses.color_pair(1))
            player = playerSet(saves, currentSaveFile)
            rooms.Room.roomLoadAll(saves, currentSaveFile)
            loadedFile = 1
            loadScreen = False
          else:
            nextLine()
            stdscr.addstr("That file does not have a save in it", curses.color_pair(1))

        elif cursorPos == 3:
          if saves[2]["Used"] == True:
            currentSaveFile = 2
            nextLine()
            stdscr.addstr("You have selected file 3", curses.color_pair(1))
            player = playerSet(saves, currentSaveFile)
            rooms.Room.roomLoadAll(saves, currentSaveFile)
            loadedFile = 1
            loadScreen = False
          else:
            nextLine()
            stdscr.addstr("That file does not have a save in it", curses.color_pair(1))

        elif cursorPos == 5:
          titleScreen = True
          newScreen = False
          loadScreen = False

      elif loadMovement == "\x1b":
        gameRunning = False
        titleScreen = False
        newScreen = False
        loadScreen = False
        stdscr.erase()
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        break

  stdscr.clear()
  #player start position
  """
  if loadedFile != 1:
    playercoords = [1,1]
    """
  playercoords = [1,1]
  tobeplayercoords = copy(playercoords)

  currentRoom = rooms.startRoom

  #Main Game Loop
  firstClear = 1
  interactables = 4
  while gameRunning == True or battling == True:
    while gameRunning:
      saveInfo(player, currentRoom, saves, currentSaveFile)
      rooms.Room.roomSaveAll(saves, currentSaveFile)
      roomInfoException = "There is no room info"
      rooms.conditionCheckAll(player)
      currentRoom.printRoom(playercoords)
      stdscr.addstr(str(saves[currentSaveFile]["roomInfo"].get(0+1)))
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
        titleScreen = False
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        with open("saves", "w") as output:
          output.write(json.dumps(saves))
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