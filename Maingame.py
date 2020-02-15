import sys
import termios
import tty
from copy import copy

#uses old 1980's programming crap to not buffer inputs from keyboard
def getchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


#playing area size:
playingHeight = 10
playingWidth = 20
#actual width: width set by user - 1
#recommend changing width to double height

#player start position
playercoords = [1,1]
tobeplayercoords = [1,1]

#add any obstacles here
#change obstacles number the more you have
obstacles = 3
wall1 = [2,5]
wall2 = [7,2]
wall3 = [3,3]

class Room:
    
    def __init__(self, layout):
        self.layout = layout
        
    def print_room(self, playercoords):
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
            
    def validmove(self, playercoords, tobeplayercoords):
        line_player_is_on = self.layout[tobeplayercoords[1]]
        print ('theline '+line_player_is_on)
        space_player_is_on = line_player_is_on[tobeplayercoords[0]]
        print ("space the player is on: |{}|.".format(space_player_is_on))
        if space_player_is_on == ' ':
            print ("coords SHOULD change")
            return True
        return False


dungeon = Room([
    '|--------------|',
    '|              |',
    '|              ]',
    '|              |',
    '|--------------|',
])

dungeon_east1 = Room([
    '|--------------|',
    '|              |',
    '[          |   |',
    '|  |   C       |',
    '|--------------|',
])
"""
if current_room.validmove(playercoords, tobeplayercoords):
    save_coords()
"""

"""
for i in range (playingWidth+2):
        print ("-",end="")
    print ("\n",end="")
    for i in range (1,playingHeight):
        if playercoords[1] == i:
            print ("|",end="")
            for j in range (playercoords[0]-1):
                print ("",end=" ")
            print ("P",end=" ")
            for j in range (playingWidth - playercoords[0]-1):
                print ("",end=" ")
            print ("|")
        else:
            print ("|",end="")
            for j in range (playingWidth):
                print (" ",end="")
            print ("|")
    for i in range (playingWidth+2):
        print ("-",end="")
"""
nerd = True
while nerd:
    dungeon.print_room(playercoords)
    print (playercoords)
    print (tobeplayercoords)
    print ("\n\n\nw, a, s, or d")
    movement = getchar()
    if movement == 'w':
        tobeplayercoords[1] -= 1
        
    if movement == 'a':
        tobeplayercoords[0] -= 1
        
    if movement == 's':
        tobeplayercoords[1] += 1
        
    if movement == 'd':
        tobeplayercoords[0] += 1
        
    if dungeon.validmove(playercoords,tobeplayercoords):
        playercoords = copy(tobeplayercoords)
    else:
        tobeplayercoords = copy(playercoords)
    x= input("he")
    print("\033c", end="")