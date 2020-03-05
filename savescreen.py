loadScreenLayout1 = [
  "                                              ",
  "                                              ",
  "                                              ",
  "       File 1 ◄     File 2       File 3       ",
  "                                              ",
  "                                              ",
  "               Back      Clear                ",
  "                                              ",
]
loadScreenLayout2 = [
  "                                              ",
  "                                              ",
  "                                              ",
  "       File 1       File 2 ◄     File 3       ",
  "                                              ",
  "                                              ",
  "               Back      Clear                ",
  "                                              ",
]
loadScreenLayout3 = [
  "                                              ",
  "                                              ",
  "                                              ",
  "       File 1       File 2       File 3 ◄     ",
  "                                              ",
  "                                              ",
  "               Back      Clear                ",
  "                                              ",
]
loadScreenLayout4 = [
  "                                              ",
  "                                              ",
  "                                              ",
  "       File 1       File 2       File 3       ",
  "                                              ",
  "                                              ",
  "               Back      Clear ◄              ",
  "                                              ",
]
loadScreenLayout5 = [
  "                                              ",
  "                                              ",
  "                                              ",
  "       File 1       File 2       File 3       ",
  "                                              ",
  "                                              ",
  "               Back ◄    Clear                ",
  "                                              ",
]
newScreenLayout1 = [
  "                                              ",
  "                                              ",
  "                                              ",
  "       File 1 ◄     File 2       File 3       ",
  "                                              ",
  "                                              ",
  "                     Back                     ",
  "                                              ",
]
newScreenLayout2 = [
  "                                              ",
  "                                              ",
  "                                              ",
  "       File 1       File 2 ◄     File 3       ",
  "                                              ",
  "                                              ",
  "                     Back                     ",
  "                                              ",
]
newScreenLayout3 = [
  "                                              ",
  "                                              ",
  "                                              ",
  "       File 1       File 2       File 3 ◄     ",
  "                                              ",
  "                                              ",
  "                     Back                     ",
  "                                              ",
]
newScreenLayout4 = [
  "                                              ",
  "                                              ",
  "                                              ",
  "       File 1       File 2       File 3       ",
  "                                              ",
  "                                              ",
  "                     Back ◄                   ",
  "                                              ",
]

def printLoadScreen(position):
  from Maingame import stdscr
  from Maingame import curses
  from Maingame import nextLine
  curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
  if position == 1:
    for lineno, line in enumerate(loadScreenLayout1):
      stdscr.addstr (loadScreenLayout1[lineno], curses.color_pair(1))
      nextLine()
  elif position == 2:
    for lineno, line in enumerate(loadScreenLayout2):
      stdscr.addstr (loadScreenLayout2[lineno], curses.color_pair(1))
      nextLine()
  elif position == 3:
    for lineno, line in enumerate(loadScreenLayout3):
      stdscr.addstr (loadScreenLayout3[lineno], curses.color_pair(1))
      nextLine()
  elif position == 4:
    for lineno, line in enumerate(loadScreenLayout4):
      stdscr.addstr (loadScreenLayout4[lineno], curses.color_pair(1))
      nextLine()
  elif position == 5:
    for lineno, line in enumerate(loadScreenLayout5):
      stdscr.addstr (loadScreenLayout5[lineno], curses.color_pair(1))
      nextLine()

def printNewScreen(position):
  from Maingame import stdscr
  from Maingame import nextLine
  from Maingame import curses
  curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
  if position == 1:
    for lineno, line in enumerate(newScreenLayout1):
      stdscr.addstr (newScreenLayout1[lineno], curses.color_pair(1))
      nextLine()
  elif position == 2:
    for lineno, line in enumerate(newScreenLayout2):
      stdscr.addstr (newScreenLayout2[lineno], curses.color_pair(1))
      nextLine()
  elif position == 3:
    for lineno, line in enumerate(newScreenLayout3):
      stdscr.addstr (newScreenLayout3[lineno], curses.color_pair(1))
      nextLine()
  elif position == 4:
    for lineno, line in enumerate(newScreenLayout4):
      stdscr.addstr (newScreenLayout4[lineno], curses.color_pair(1))
      nextLine()