class Hero:

    # Inherence
    def __init__(self, name, health, attackPower, defenseNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.defenseNumber = defenseNumber 

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}")
        lawan.diserang(self, self.attackPower)

    def diserang(self, lawan, attackPower_lawan):
        print(f"{self.name} diserang {lawan.name}")
        attack_diterima = attackPower_lawan / self.defenseNumber
        print(f"Serangan terasa {attack_diterima}")
        self.health -= attack_diterima
        print(f"Darah {self.name} tersisa {self.health}")

sniper = Hero('sniper', 100, 45, 2)
rikimaru = Hero('rikimaru', 100, 67, 2)

rikimaru.serang(sniper)
print("\n")
sniper.serang(rikimaru)

