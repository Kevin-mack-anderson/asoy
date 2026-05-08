class Hero:

  def __init__(self, name, health, attackPower):
    self.__name = name
    self.__health = health
    self.__attpower = attackPower

  # Getter
  def getName(self):
    return self.__name

  def getHealth(self, __health):
    return self.__health

miya = Hero("Miya", 100, 15)

print(miya.getName())