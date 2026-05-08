# # Latihan 1: Validasi Dasar (Level: Mudah)
# Skenario: Kamu sedang membuat aplikasi pemantau cuaca. Kamu memiliki kelas Suhu yang menyimpan nilai suhu dalam Celcius. Secara sains, suhu tidak mungkin berada di bawah Nol Mutlak (-273.15 derajat Celcius).

# Tugas:
# Buat kelas Suhu dengan metode __init__ yang menerima parameter celcius.
# Simpan nilai tersebut dalam atribut protected (misalnya _celcius).
# Buat Getter menggunakan @property untuk mengambil nilai suhu.
# Buat Setter untuk memastikan bahwa jika ada yang mencoba memasukkan nilai di bawah -273.15, program akan memunculkan error: ValueError("Suhu tidak boleh di bawah nol mutlak!").


class Suhu:

  celci = 0;

  def __init__(self, suhu):
    self.__suhu = suhu


  # Getter
  @property
  def nilai(cls):
    return cls.__suhu
  
  # Setter
  @nilai.setter
  def inputan(self, input):
    self.__suhu = input

    if self.__suhu < -273.05:
      print("VALUE ERROR 0 MUTLAK")


suhunya = Suhu(0)
print(suhunya.nilai)
print(suhunya.inputan(0.))
  