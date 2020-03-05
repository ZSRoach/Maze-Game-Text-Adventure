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
    dmg = (random.randint(3,attacker.attack))
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
  def attack(player, enemy):
    from Maingame import stdscr
    attackChance = random.randint(1,player.attack)
    defenseChance = enemy.defense
    if attackChance >= defenseChance:
      damage = player.attack * 3
      damage -= enemy.defense
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
#Definition of skeleton - ranged enemy - (Inherits from entitiy) - Enemy class type
class Skeleton(Entity):
  hostile = False
  name = "Skeletini"
#Def of zombie - Stronger version of Goblin - (Inherits from entity) - Enemy class type
class Zombie(Entity):
  hostile = False
  name = "Zombini"
#Def of Golem - Stronger version of Zombie - (Inherits from Entity) - enemy class type
class Golem(Entity):
  hostile = False
  name = "Golini"
class Boss(Entity):
  name1 = "Turkey Panini"
  name2 = "Parmesan Tortellini"
  name3 = "Spinach Fettuccine"
  final = "Spicy Pasta Linguine"