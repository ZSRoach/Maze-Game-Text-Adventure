saveScreenLayout1 = [
  "                                              ",
  "                                              ",
  "                                              ",
  "       File 1 ◄     File 2       File 3       ",
  "                                              ",
  "                                              ",
  "                     Clear                    ",
  "                                              ",
]
saveScreenLayout2 = [
  "                                              ",
  "                                              ",
  "                                              ",
  "       File 1       File 2 ◄     File 3       ",
  "                                              ",
  "                                              ",
  "                     Clear                    ",
  "                                              ",
]
saveScreenLayout3 = [
  "                                              ",
  "                                              ",
  "                                              ",
  "       File 1       File 2       File 3 ◄     ",
  "                                              ",
  "                                              ",
  "                     Clear                    ",
  "                                              ",
]
saveScreenLayout4 = [
  "                                              ",
  "                                              ",
  "                                              ",
  "       File 1       File 2       File 3       ",
  "                                              ",
  "                                              ",
  "                     Clear ◄                  ",
  "                                              ",
]
saveScreenLayout5 = [
  "                                              ",
  "                                              ",
  "                                              ",
  "       File 1 ◄     File 2       File 3       ",
  "                                              ",
  "                                              ",
  "                                              ",
  "                                              ",
]
saveScreenLayout6 = [
  "                                              ",
  "                                              ",
  "                                              ",
  "       File 1       File 2 ◄     File 3       ",
  "                                              ",
  "                                              ",
  "                                              ",
  "                                              ",
]
saveScreenLayout7 = [
  "                                              ",
  "                                              ",
  "                                              ",
  "       File 1       File 2       File 3 ◄     ",
  "                                              ",
  "                                              ",
  "                                              ",
  "                                              ",
]
def printSaveScreen(position):
  from Maingame import stdscr
  from Maingame import curses
  from Maingame import nextLine
  curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
  if position == 1:
    for lineno, line in enumerate(saveScreenLayout1):
      stdscr.addstr (saveScreenLayout1[lineno], curses.color_pair(1))
      nextLine()
  elif position == 2:
    for lineno, line in enumerate(saveScreenLayout2):
      stdscr.addstr (saveScreenLayout2[lineno], curses.color_pair(1))
      nextLine()
  elif position == 3:
    for lineno, line in enumerate(saveScreenLayout3):
      stdscr.addstr (saveScreenLayout3[lineno], curses.color_pair(1))
      nextLine()
  elif position == 4:
    for lineno, line in enumerate(saveScreenLayout4):
      stdscr.addstr (saveScreenLayout4[lineno], curses.color_pair(1))
      nextLine()
  elif position == 5:
    for lineno, line in enumerate(saveScreenLayout5):
      stdscr.addstr (saveScreenLayout5[lineno], curses.color_pair(1))
      nextLine()
  elif position == 6:
    for lineno, line in enumerate(saveScreenLayout6):
      stdscr.addstr (saveScreenLayout6[lineno], curses.color_pair(1))
      nextLine()
  elif position == 7:
    for lineno, line in enumerate(saveScreenLayout7):
      stdscr.addstr (saveScreenLayout7[lineno], curses.color_pair(1))
      nextLine()