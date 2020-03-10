titleScreenLayout1 = [
  "                                              ",
  "                                              ",
  "                 MAZE MASSACRE                ",
  "        Copyright © Z&S Productions 2020      ",
  "                                              ",
  "                   NEW SAVE   ◄               ",
  "                  LOAD  SAVE                  ",
  "                                              ",
]
titleScreenLayout2 = [
  "                                              ",
  "                                              ",
  "                 MAZE MASSACRE                ",
  "        Copyright © Z&S Productions 2020      ",
  "                                              ",
  "                   NEW SAVE                   ",
  "                  LOAD  SAVE  ◄               ",
  "                                              ",
]
def printTitleScreen(position):
  from Maingame import stdscr
  from Maingame import curses
  from Maingame import nextLine
  curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
  if position == 1:
    for lineno, line in enumerate(titleScreenLayout1):
     stdscr.addstr (titleScreenLayout1[lineno], curses.color_pair(1))
     nextLine()
  elif position == 2:
    for lineno, line in enumerate(titleScreenLayout2):
     stdscr.addstr (titleScreenLayout2[lineno], curses.color_pair(1))
     nextLine()

def saveScreen():
  from Maingame import stdscr
  from Maingame import curses
  curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
  stdscr.addstr ("saving... Wait 10 seconds before closing ", curses.color_pair(1))
