import Entities
def classChoice():
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
  stdscr.refresh()
  classChoice = 7
  chosenCorrectly = True
  while chosenCorrectly:
    classChoice = getchar()
    if classChoice == "1" or classChoice == "2" or classChoice == "3" or classChoice =="4":
      chosenCorrectly = False
  if classChoice == "1":
    nextLine()
    nextLine()
    stdscr.addstr("Name your warrior: ",curses.color_pair(1))
    stdscr.refresh()
    nameChoice = stdscr.getstr()
    nameChoice = nameChoice.decode("utf-8")
    player = Entities.Warrior(nameChoice)
    return player
  elif classChoice == "2":
    nextLine()
    nextLine()
    stdscr.addstr("Name your sorcerer: ",curses.color_pair(1))
    stdscr.refresh()
    nameChoice = stdscr.getstr()
    nameChoice = nameChoice.decode("utf-8")
    player = Entities.Sorcerer(nameChoice)
    stdscr.addstr("character has been made",curses.color_pair(1))
    return player
  elif classChoice == "3":
    nextLine()
    nextLine()
    stdscr.addstr("Name your rogue: ",curses.color_pair(1))
    stdscr.refresh()
    nameChoice = stdscr.getstr()
    nameChoice = nameChoice.decode("utf-8")
    player = Entities.Rogue(nameChoice)
    return player
  elif classChoice == "4":
    nextLine()
    nextLine()
    stdscr.addstr("Name your necromancer: ",curses.color_pair(1))
    stdscr.refresh()
    nameChoice = stdscr.getstr()
    nameChoice = nameChoice.decode("utf-8") 
    player = Entities.Necromancer(nameChoice)
    return player
