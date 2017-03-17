class Minion():
    def __init__(self, hp, dmg):
        print ('Minion constructor called')
        self.health = hp
        self.damage = dmg

class Champ(Minion):
    def __init__(self,hp,dmg, mp, skill):
        print ('Champ constructor called')
        Minion.__init__(self, hp, dmg)
        self.mana = mp
        self.spell = skill

purpleCaster = Minion('200', '500')
print (purpleCaster.damage)

Garen = Champ('1000', '500', '100', 'Decicive Strike')
print (Garen.mana)
print (Garen.spell)
