import random
xpPerLevel = ["100","200",]
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
  def levelUp(leveler):
    print ("You leveled up to level "+str((leveler.level)+1)+"!!")
    leveler.level += 1
  def fool(self, fooled):
    print("you've been fooled "+fooled.name)
  pass

#definition of sorcerer - player subclass - (inherits from entity, and player) - user class type
class Sorcerer(Player):
  isSorcerer = 1
  mana = 20
  spells = 0

#definition of warrior - player subclass - (inherits from entity, and player) - user class type
class Warrior(Player):
  isWarrior = 1
  oneHandedWeapons = 1
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