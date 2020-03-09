import random
xpPerLevel = ["100","100","150","200","300","400","500","600","700","800","900","1000","1150","1300","1550","1750","1900","2000","2600"]
xpAtLevel = ["0","100","200","350","550","850","1250","2350","3050","3850","4750","5750","6900","8200","9750","11500","13400","15400","18000"]
class Entity():
  health = 0
  attack = 0
  defense = 0
  speed = 0 
    
  #definition of basic entity methods 
  def basicAttack(attacker, target):
    attackChance = random.randint(1,attacker.attack)
    if attackChance >= target.defense:
      dmg = (attacker.attack * 3) - target.defense
    else:
      dmg = attacker.attack - (target.defense * 0.5)
    if target.isBlocking == True:
      dmg *= .75
    dmg = int(dmg)
    target.health -= dmg
  pass

#definition of main player class (inherits traits from entity) - user character
class Player(Entity):
  def __init__(self, name):
    self.name = name
  weapons = 0
  skills = 0
  level = 1
  xp = 0
  upgradePoints = 0
  isInteracting = False
  isBlocking = False
  def levelUp(leveler):
    from Maingame import stdscr
    stdscr.addstr ("You leveled up to level "+str((leveler.level)+1)+"!!")
    leveler.level += 1
  def fool(self, fooled):
    from Maingame import stdscr
    stdscr.addstr("you've been fooled "+fooled.name)
  def normalAttack(player, enemy):
    from Maingame import stdscr
    attackChance = random.randint(1,player.attack)
    defenseChance = enemy.defense
    if attackChance >= defenseChance:
      damage = player.attack * 3
      damage -= enemy.defense
      if enemy.isBlocking == True:
        damage *= 0.75
        damage = int(damage)
      enemy.health -= damage
    else:
      damage = player.attack - (enemy.defense / 2)
      enemy.health -= damage
    stdscr.addstr("You attacked the "+enemy.name+" for "+str(damage)+" damage!")
  def block(player):
    from Maingame import stdscr
    from Maingame import getchar
    from Maingame import curses
    stdscr.addstr("Do you want to block? You'll take 3/4 damage but can't attack",curses.color_pair(1))
    stdscr.addstr("1 if you want to block")
    block = getchar()
    if block == 1:
      player.isBlocking = True
  pass

#definition of sorcerer - player subclass - (inherits from entity, and player) - user class type
class Sorcerer(Player):
  isSorcerer = 1
  mana = 20
  spells = 0
  manaRegen = 5
  spellDamage = 1

#definition of warrior - player subclass - (inherits from entity, and player) - user class type
class Warrior(Player):
  isWarrior = 1
  twoHanded = False

#definition of rogue - player subclass - (inherits from entity, and player) - user class type
class Rogue(Player):
  isRogue = 1
  evadeChance = 3 #evasion calculation: random number 1 - 100; if random number  >= 100-evadechance, take no dmg
  stealth = 1
    
#definition of necromancer - player subclass - (inherits from entity, and player) - user class type
class Necromancer(Player):
  isNecromancer = 1
  maxMinions = 0
  currentMinions = 0
  currentMinionsAlive = 0
  minionHealth = 0
  minionAttack = 0

class Minion(Entity):
  health = 0

#definition of goblin - main throwaway generic enemy - (inherits from entity) - enemy class type
class Goblin(Entity):
  hostile = False
  name = "Goblini"
  health = 50
  attack = 8
  defense = 8
  speed = 5
#Definition of skeleton - ranged enemy - (Inherits from entitiy) - Enemy class type
class Skeleton(Entity):
  hostile = False
  name = "Skeletini"
  health = 75
  attack = 15
  defense = 20
  speed = 10
  def rangedAttack(skeleton,player):
    attackChance = random.randint(1,skeleton.attack + 5)
    if attackChance >= player.defense:
      dmg = (skeleton.attack + 5) - player.defense
    else:
      dmg = skeleton.attack + 5 - (player.defense * .5)
      dmg = int(dmg)
    missChance = random.randint(1,player.speed)
    if missChance >= skeleton.speed:
      dmg = 0
    player.health -= dmg
#Def of zombie - Stronger version of Goblin - (Inherits from entity) - Enemy class type
class Zombie(Entity):
  hostile = False
  name = "Zombini"
  health = 115
  attack = 25
  defense = 25
  speed = 12
  def bite(attacker, player):
    biteChance = random.randint(1,attacker.speed + 8)
    missChance = random.randint(1,player.speed)
    if biteChance >= missChance:
      player.health -= (1/5) * player.health
#Def of Golem - Stronger version of Zombie - (Inherits from Entity) - enemy class type
class Golem(Entity):
  hostile = False
  name = "Golini"
  health = 250
  attack = 32
  defense = 35
  speed = 15
  def strength(attacker, player):
    print("Placeholder")
    strengthMultiplier = random.randint(1,4)
    attackChance = random.randint(1,attacker.attack + 10)
    if attackChance >= player.defense:
      dmg = (attacker.attack + 10) - player.defense
      dmg *= strengthMultiplier
    else:
      dmg = attacker.attack - (player.defense * .75)
      dmg = int(dmg)
      dmg *= strengthMultiplier
    player.health -= dmg
class Boss(Entity):
  def __init__(self, health, attack, defense, speed, name):
    self.health = health
    self.attack = attack
    self.defense = defense
    self.speed = speed
    self.name = name
#name1 = "Turkey Panini"
#name2 = "Parmesan Tortellini"
#name3 = "Spinach Fettuccine"
#final = "Spicy Pasta Linguine"