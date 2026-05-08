class Hero:
    #Class Variable
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # Istance Variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    # Void Function, method tanpa return
    def siapa(self):
        print("Namaku adalah" + self.name)

    # Method dengan argumen
    def healthUp(self, up):
        self.health += up

    # Method dengan return
    def getHealth(self):
        return self.health
        


hero1 = Hero('sniper', 100, 10, 5)
hero1 = Hero('Udin', 50, 10, 5)

hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealth)