from termcolor import colored
from Maingame import stdscr
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
  if position == 1:
    for lineno, line in enumerate(titleScreenLayout1):
     stdscr.addstr (colored(titleScreenLayout1[lineno], "white", attrs=["reverse"]))
  elif position == 2:
    for lineno, line in enumerate(titleScreenLayout2):
     stdscr.addstr (colored(titleScreenLayout2[lineno], "white", attrs=["reverse"]))

def saveScreen():
 stdscr.addstr ("saving... Wait 10 seconds before closing ")