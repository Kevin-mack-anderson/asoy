class AntrianLayanan:
  
  def __init__(self):
    self.queue = []

    # Menambahkan Pelanggan
  def masuk_antrian(self, nama_pelanggan):
      self.queue.append(nama_pelanggan)
      print(f"Pelanggan {nama_pelanggan} Masuk Antrian")

      # Melayani Pelanggan
  def layani_pelanggan(self):
        if not self.is_empty():
          if not self.is_empty():
            pelanggan = self.queue.pop(0)
            print(f"Melayani : {pelanggan}")
            return pelanggan
          else:
            print("Antrian Kosong. Tidak ada yang dilayani")
            return None
          
      # Cek antrian kosong
  def is_empty(self):
        print(f"Antrian saat ini: {self.queue}")
antrian = AntrianLayanan()
print(antrian.layani_pelanggan())
nama = "ucup"
print(nama.layani_pelanggan())