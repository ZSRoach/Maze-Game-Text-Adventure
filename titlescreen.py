from termcolor import colored
titleScreenLayout1 = [
  "                                              ",
  "                                              ",
  "                 MAZE MASSACRE                ",
  "        Copyright © Z&S Productions 2020      ",
  "                                              ",
  "                     START    ◄               ",
  "                   SAVE CODE                  ",
  "                                              ",
]
titleScreenLayout2 = [
  "                                              ",
  "                                              ",
  "                 MAZE MASSACRE                ",
  "        Copyright © Z&S Productions 2020      ",
  "                                              ",
  "                     START                    ",
  "                   SAVE CODE  ◄               ",
  "                                              ",
]
def printTitleScreen(position):
  from Maingame import stdscr
  from Maingame import curses
  curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
  if position == 1:
    for lineno, line in enumerate(titleScreenLayout1):
     stdscr.addstr (titleScreenLayout1[lineno], curses.color_pair(1))
     pos = stdscr.getyx()
     ypos = pos[0]
     xpos= pos[1]
     ypos+=1
     stdscr.move(ypos,0)
  elif position == 2:
    for lineno, line in enumerate(titleScreenLayout2):
     stdscr.addstr (titleScreenLayout2[lineno], curses.color_pair(1))
     pos = stdscr.getyx()
     ypos = pos[0]
     xpos= pos[1]
     ypos+=1
     stdscr.move(ypos,0)

def saveScreen():
  from Maingame import stdscr
  from Maingame import curses
  curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
  stdscr.addstr ("saving... Wait 10 seconds before closing ", curses.color_pair(1))
