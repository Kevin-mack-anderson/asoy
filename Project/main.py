import queue
import threading
import time
import random
import pyttsx3
import os
from datetime import date

os.system("cls")

#Insialisasi Pesan orderan
grs = "-"*50
# Inisialisasi Penampung
antrean_utama = queue.PriorityQueue()

# Data web (scheduling)
web_schedule_list = [
  {"item": "Kopi Aren (web)", "waktu": time.strftime("%H:%M", time.localtime(time.time() + 60))},
  {"item": "French Fries (web)", "waktu": time.strftime("%H:%M", time.localtime(time.time() + 60))},
]

# Fungsi Suara
def speak(text):
  try:
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id )
    engine.setProperty("rate", 250)
    engine.say(text)
    engine.runAndWait()
  except:
    pass

# Class Pesanan
class Pesanan:

  def __init__(self, asal, nama_pesanan):
    self.asal = asal
    self.nama_psn = nama_pesanan
    # 9/5/2026 11:14
    self.data_durasi = {
      "Kopi Kampung":10,
      "Blue Ocean":12,
      "Pasta":15,
      "French fries":15,
      "Milktea":10,
      "Butterscotch":10,
      "Kopi Aren":11
      }
    
    self.durasi = self.hitung_total_durasi(self.nama_psn)
  def hitung_total_durasi(self, nama):
      total = 0
      items = nama.split("&")
      for item in items:
        total += self.data_durasi.get(item, 7)
        return total
    # =====
   

  def __repr__(self):
    return f"[{self.asal}] {self.nama_psn}"
  

# fungsi thread ojol
def generator_ojol():
  menu = ["Kopi Kampung", "Blueocean", "Milktea"]
  while True:
    time.sleep(random.randint(12,19))
    item = random.choice(menu)
    order = Pesanan("OJOL",item)

    # Priority 1 Ojol
    antrean_utama.put((1, time.time(), order))

    print(f"{grs}\n\t\t[NEW CHECKER] \n{grs}\n{date.today()} \t\t\t\t    {time.strftime("%H:%M")}\n{order}\nPrioritas\t\t\t\t\t1\nSegera Diproses! \n{grs}")
    threading.Thread(target= speak, args= (f"PESANAN BARU DARI OJEK ONLINE , {item}",), daemon=True).start()

# Generator Walk In
def generator_walkIn():
  menu = ["Kopi Aren", "Butterscotch", "Pasta"]
  while True:
    time.sleep(random.randint(7,15))
    item = random.choice(menu)
    order = Pesanan("WALK-IN", item)

    # Scale Priority = 2
    antrean_utama.put((2, time.time(), order))

    print(f"{grs}\n\t\t[NEW CHECKER] \n{grs}\n{date.today()} \t\t\t\t    {time.strftime("%H:%M")}\n{order}\nPrioritas\t\t\t\t\t2\nSegera Diproses! \n{grs}")
    threading.Thread(target= speak, args= (f"PESANAN BARU WALK-IN, {item}",), daemon=True).start()

# Scheduler
def scheduler_web():
  while True:
    current_time = time.strftime("%H:%M")
    for order_data in web_schedule_list[:]:
      if order_data["waktu"] == current_time:
        order = Pesanan(order_data["item"], "WEB")

        # Scale Priority = 3
        antrean_utama.put((3, time.time(), order))

        print(f"\n\t\t[CHECKER JADWAL]\n {grs}\n {order}\n masuk antrian sesuai jadwal.\n{grs}")
        threading.Thread(target= speak, args= (f"SAATNYA PROSES PESANAN WEB{order_data["item"]}",), daemon=True).start()
        web_schedule_list.remove(order_data)

    time.sleep(10)


# Thread Pemroses
NAMA = "Ucup"
# Ada pembaruan
def barista_eksekutor():
  # Penambahan fitur di barista
  while True:
    if not antrean_utama.empty():
      prio, time_stamp, data = antrean_utama.get()

      print(f"\n >>Barista: { NAMA} SEDANG MEMBUAT: {data} (Prioritas: {prio})  (DURASI: {data.durasi})<<<<")
      time.sleep(data.durasi)
      print(f"!!!!!Barista:{ NAMA} PESANAN {data} SELESAI!!!!!!")

      antrean_utama.task_done()
   
    else:
      time.sleep(1)

# Main exe
if __name__ == "__main__":
  print("=== SISTEM OTOMASI KAFE DIMULAI ===")
  print("Tekan Ctrl+C untuk berhenti. \n")

# Fitur Nama Barista  
handler1 = threading.Thread(target=barista_eksekutor, daemon=True)
handler2 = threading.Thread(target=barista_eksekutor, daemon=True)
handler3 = threading.Thread(target=barista_eksekutor, daemon=True)
# Inisialisasi thread
t_ojol = threading.Thread(target=generator_ojol, daemon=True)
t_walkin = threading.Thread(target=generator_walkIn, daemon=True)
t_web = threading.Thread(target=scheduler_web, daemon=True)
# turn on
t_ojol.start()
t_walkin.start()
t_web.start()
handler1.start()
handler2.start()
handler3.start()


try: 
  while True:
    time.sleep(1)
except KeyboardInterrupt:
  print("\n Sistem dimatikan oleh user")
\

