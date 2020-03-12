#Will eventually become the fighting mechanic
import random
from Entities import Entity
from Entities import Player
from Entities import Sorcerer
from Entities import Warrior
from Entities import Rogue
from Entities import Necromancer
from Entities import Minion
from Entities import Goblin
from Entities import Skeleton
from Entities import Zombie
from Entities import Golem
from Entities import Boss
def enemyMove(enemy, player):
  if enemy.isGoblin == 1:
    enemy.basicAttack(enemy, player)
  elif enemy.isSkeleton == 1:
    move = random.randint(1,2)
    if move == 1:
      Entity.basicAttack(enemy, player)
    else:
      Entity.rangedAttack(enemy, player)
  elif enemy.isZombie == 1:
    move = random.randint(1,2)
    if move == 1:
      Entity.basicAttack(enemy, player)
    else:
      Entity.bite(enemy, player)
  else:
    move = random.randint(1,2)
    if move == 1:
      Entity.basicAttack(enemy, player)
    else:
      Entity.strength(enemy, player)
def battle(player, enemy):
  while player.health > 0 and enemy.health > 0:
    if player.speed > enemy.speed:
      player.block(player, enemy)
      player.normalAttack(player, enemy)
      enemyMove(enemy, player)
    else:
      enemyMove(enemy,player)
      player.block(player, enemy)
      player.normalAttack(player, enemy)
