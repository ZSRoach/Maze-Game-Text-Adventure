import Entities
def classChoice(player):
  from Maingame import stdscr
  from Maingame import curses
  from Maingame import nextLine
  from Maingame import getchar
  doLoop = True
  nextLine()
  stdscr.addstr("Choose your class (1, 2, 3, or 4):",curses.color_pair(1))
  nextLine()
  nextLine()
  stdscr.addstr("1) Warrior",curses.color_pair(1))
  nextLine()
  nextLine()
  stdscr.addstr("2) Sorcerer",curses.color_pair(1))
  nextLine()
  nextLine()
  stdscr.addstr("3) Rogue",curses.color_pair(1))
  nextLine()
  nextLine()
  stdscr.addstr("4) Necromancer",curses.color_pair(1))
  classChoice = getchar()
  while doLoop:
    global player
    if classChoice == "1":
      nextLine()
      nextLine()
      stdscr.addstr("Name your warrior: ",curses.color_pair(1))
      nameChoice = curses.getstr()
      player = Entities.Warrior(nameChoice)
      doLoop = False
    elif classChoice == "2":
      nextLine()
      nextLine()
      stdscr.addstr("Name your sorcerer: ",curses.color_pair(1))
      nameChoice = curses.getstr()
      player = Entities.Sorcerer(nameChoice)
      doLoop = False
    elif classChoice == "3":
      nextLine()
      nextLine()
      stdscr.addstr("Name your rogue: ",curses.color_pair(1))
      nameChoice = curses.getstr()
      player = Entities.Rogue(nameChoice)
      doLoop = False
    elif classChoice == "4":
      nextLine()
      nextLine()
      stdscr.addstr("Name your necromancer: ",curses.color_pair(1))
      nameChoice = curses.getstr()
      player = Entities.Necromancer(nameChoice)
      doLoop = False
