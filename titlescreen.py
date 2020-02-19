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
  "                   SAVE CODE  ◄                ",
  "                                              ",
]
def printTitleScreen(position):
  if position == 1:
    for lineno, line in enumerate(titleScreenLayout1):
      print (titleScreenLayout1[lineno])
  elif position == 2:
    for lineno, line in enumerate(titleScreenLayout2):
      print (titleScreenLayout2[lineno])