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
    upgradePoints = 0
    def levelUp(leveler):
        print ("You leveled up to level "+str((leveler.level)+1)+"!!")
        leveler.level += 1
    def fool(self, fooled):
        print("you've been fooled "+fooled.name)
    pass

#definition of sorcerer - player subclass - (inherits from entity, and player) - user class type
class Sorcerer(Player):
    mana = 3
    spells = 0

#definition of warrior - player subclass - (inherits from entity, and player) - user class type
class Warrior(Player):
    oneHandedWeapons = 1
    twoHanded = False

#definition of rogue - player subclass - (inherits from entity, and player) - user class type
class Rogue(Player):
    evadeChance = 5 #evasion calculation: random number 1 - 100; if random number  >= 100-evadechance, take no dmg
    stealth = 1
    
#definition of necromancer - player subclass - (inherits from entity, and player) - user class type
class Necromancer(Player):
    minionTypes = 0
    maxMinions = 0
    currentMinions = 0
    minionHealth = 0
    minionAttack = 0
    
#definition of goblin - main throwaway generic enemy - (inherits from entity) - enemy class type
class Goblin(Entity):
    hostile = False