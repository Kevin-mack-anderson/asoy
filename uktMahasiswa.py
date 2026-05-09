import os

os.system("cls")
class Ukt_Mahasiswa:

  
  def __init__(self, nama_mhs, status:0, nominalBayar, NIM):
    self.nama = nama_mhs
    self.status = status
    self.nominal = nominalBayar
    self.nim = NIM
  
  # Fungsi cek status
  
  def cek_status(self):
    if self.status == 0:
       print("ANDA BELUM BAYAR UKT")
    elif self.status == self.nominal:
       print("UKT ANDA SUDAH LUNAS")
    else:
      print("apalah")
    

  
  # Fungsi Bayar
  def bayar(self):
    bayar = 0
    autentikasi = int(input("Silahkan Masukan NIM Anda: "))
    if autentikasi == self.nim:
      bayar = int(input("Masukan nominal yang sesuai (100000) = "))
      if bayar < self.nominal:
        print("Kurang bos")
      else:
        hasil = self.nominal =- bayar
        print("Pembayaran Berhasil!!") 
        self.status += hasil
      return hasil
    

mhs = Ukt_Mahasiswa("Ucup surucup", 0, 100000, 12123)
# Pilihan
while True:
  
  pilih = input("Mau pilih apa 1= cekstatus 2=bayar : ")
  if pilih == "1":
    mhs.cek_status()
  elif pilih == "2":
    mhs.bayar()

  # exit
  pilihan = input("Apa mau lagi?(y/n):")
  if pilihan == "y":
    continue
  elif pilihan == "n":
    break
  else:
    print("pilihan tidak ada")
    break

