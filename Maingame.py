import sys
from copy import copy
import os
try:
  import termios
  import tty
except:
  import msvcrt

#uses old 1970's programming crap to not buffer inputs from keyboard
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
    roomNumber = 0
    def __init__(self, layout):
        self.layout = layout
        Room.roomNumber +=1
        self.roomNumber = Room.roomNumber

    def printRoom(self, playercoords):
        for lineno, line in enumerate(self.layout):
            playerline = line
            if playercoords[1] == lineno:
                playerline_parts = []
                for xval, char in enumerate(line):
                    if playercoords[0] == xval:
                        playerline_parts.append('P')
                    else:
                        playerline_parts.append(char)
                playerline = ''.join(playerline_parts)
            print(playerline)

    def validMove(self, playercoords, tobeplayercoords):
        line_player_is_on = self.layout[tobeplayercoords[1]]
        space_player_is_on = line_player_is_on[tobeplayercoords[0]]
        if space_player_is_on == ']' or space_player_is_on == '[' or space_player_is_on == '_' or space_player_is_on == '~':
            print("hi")
        elif space_player_is_on == ' ':
            return True
        return False


dungeon = Room([
    '|--------------|',
    '|              |',
    '|              ]',
    '|              |',
    '|--------------|',
],)

dungeon_east1 = Room([
    '|--------------|',
    '|              |',
    '[          |   |',
    '|  |   C       |',
    '|--------------|',
])

gameRunning = True
while gameRunning:
    dungeon.printRoom(playercoords)
    print (dungeon.roomNumber)
    print (dungeon_east1.roomNumber)
    print (playercoords)
    print (tobeplayercoords)
    print ("\n\n\nw, a, s, or d")
    movement = getchar()
    print (movement)
    if movement == 'w':
        tobeplayercoords[1] -= 1

    if movement == 'a':
        tobeplayercoords[0] -= 1

    if movement == 's':
        tobeplayercoords[1] += 1

    if movement == 'd':
        tobeplayercoords[0] += 1

    if dungeon.validMove(playercoords,tobeplayercoords):
        playercoords = copy(tobeplayercoords)
    else:
        tobeplayercoords = copy(playercoords)
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')
