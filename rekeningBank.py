class Rekening_bank:

  def __init__(self, namaPemilik, jumlah, saldoAwal=0,):
    self.namaPemilik = namaPemilik
    self.saldoAwal = saldoAwal
    self.jumlah = jumlah
    print(f"Rekening dengan atas nama {self.namaPemilik} berhasil dibuat, saldo:{self.saldoAwal}")

  # Fungsi setor uang
  def setor(self, jumlah):
    if jumlah > 0:
      self.saldoAwal += jumlah
      print(f"Kamu dikirimin {self.jumlah}. Total Saldo Saat Ini : {self.saldoAwal}")
    else:
      print(["[ERROR] Nominal Harus Lebih Besar Dari 0!"])

  # Fungsi tarik uang
  def tarik(self, jumlah):
    if jumlah > self.saldoAwal:
      print("[ERROR, Saldo Tidak Mencukupi]")
    elif jumlah <= 0:
      print("Nominal Penarikan Harus Lebih Besar Dari 0!")
    else:
      self.saldoAwal -= jumlah
      print(f"Penarikan Sebesar {jumlah} Telah Berhasil, Sisa Saldo Saat Ini {self.saldoAwal}")

  # Fungsi cek Saldo
  def cek(self):
    print(f"Sisa Saldo Saat Ini {self}")


rek_assa = Rekening_bank("assa", 100000)
rek_tikka = Rekening_bank("assa", 200000)


rek_assa.setor(10000)
rek_assa.tarik(10000)