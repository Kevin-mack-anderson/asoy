class Hero:

  # Memprivate class var
  __jumlah = 0;

  def __init__(self, name):
    self.__name = name
    Hero.__jumlah +=1

  # MEthod ini hanya berlaku untuk objek
  def getJumlah(self):
    return Hero.__jumlah
  
  # Method ini tidak berlaku untuk objek tetapi berlaku untuk class
  def getJumlah1():
    return Hero.__jumlah
  
  # Method static (decorator) berlaku untuk class dan objek
  @staticmethod 
  def getJumlah2():
    return Hero.__jumlah
  
  @classmethod
  def getJumlah3(cls):
    return cls.__jumlah
  
sniper = Hero('sniper')
print(Hero.getJumlah2())
rikimaru = Hero('rikimaru')
print(sniper.getJumlah2())
drownranger = Hero('drownranger')
print(sniper.getJumlah3())
