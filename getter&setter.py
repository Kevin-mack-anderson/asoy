class Hero:

  def __init__(self, name, health, armor):
    self.name = name
    self.__health = health
    self.__armor = armor


  @property
  def info(self):
    return "Name : {} \n\t Health: {}".format(self.name, self.__health)
  
  # Armor ini beda dengan armor yang diatas
  @property
  def armor(self):
    pass

  @armor.getter
  def armor(self):
    return self.__armor
  
  @armor.setter
  def armor(self, input):
    self.__armor = input

  @armor.deleter
  def armor(self):
    print('Armor di delet')
    self.__armor = None

sniper = Hero("Sniper", 100, 10)

print("Merubah info")
print(sniper.info)
sniper.name = "dadang"
print(sniper.info)

print("getter dan setter untuk __armor")
print(sniper.armor) 
sniper.armor = 50
print(sniper.armor)

print("delete armor")
del sniper.armor
print(sniper.__dict__)