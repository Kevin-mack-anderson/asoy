class Ukt_Mahasiswa:

  def __init__(self, nama_mhs, status_mhs, nominalBayar, NIM):
    self.nama = nama_mhs
    self.status = status_mhs
    self.nominal = nominalBayar
    self.nim = NIM


  # Fungsi cek status

  def cek_status(self, status):
    if status == 0:
      print(f"Anda Belum Melakukan Pembayaran UKT, Segera Lakukan!")
    elif status == self.nominal:
      print(f"Status UKT anda sudah terbayarkan!!")
  
  # Fungsi Bayar
  def bayar(self, bayar):
    autentikasi = int(input("Silahkan Masukan NIM Anda: "))
    if autentikasi is not self.nim:
      print("NIM Anda Tidak Valid!!")
    else: 
      transaksi = 