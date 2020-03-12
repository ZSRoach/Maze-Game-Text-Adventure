import random
import copy
def enemyMove(self, currentRoom, playercoords):
  randomMove = random.randint(1,4)
  badMove = True
  while badMove:
    self.toBeCoords = copy(self.coords)
    if randomMove == 1:
      self.toBeCoords[1] - 1
    if randomMove == 2:
      self.toBeCoords[0] + 1
    if randomMove == 3:
      self.toBeCoords[1] + 1
    if randomMove == 4:
      self.toBeCoords[0] - 1
    if currentRoom.validMove(self.coords, self.toBeCoords):
      if playercoords == self.toBeCoords:
        badMove = True
      else:
        badMove = False
    else:
      badMove = True
  self.coords = copy(self.toBeCoords)
