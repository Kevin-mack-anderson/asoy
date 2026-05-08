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
lihat = antrean_utama

# Data web (scheduling)
web_schedule_list = [
  {"item": "Kopi Aren (web)", "waktu": time.strftime("%H:%M", time.localtime(time.time() + 60))},
  {"item": "French Fries (web)", "waktu": time.strftime("%H:%M", time.localtime(time.time() + 60))},
]

# Fungsi Suara
def speak(text):
  try:
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()
  except:
    pass

# Class Pesanan
class Pesanan:

  def __init__(self, asal, nama_pesanan):
    self.asal = asal
    self.nama_psn = nama_pesanan
    # Penambahan fitur kecepatan membuat
    if asal == "OJOL":
      self.durasi = random.randint(10, 20)
    else: 
      self.durasi = random.randint(2, 5)

  def __repr__(self):
    return f"[{self.asal}] {self.nama_psn}"

# fungsi thread ojol
def generator_ojol():
  menu = ["Kopi Kampung", "Blue Lagon", "MilkTea"]
  while True:
    time.sleep(random.randint(7,7))
    item = random.sample(menu, k=2)
    pesanannya ="&".join(item) 
    order = Pesanan("OJOL",pesanannya )

    # Priority 1 Ojol
    antrean_utama.put((1, time.time(), order))

    print(f"{grs}\n\t\t[NEW CHECKER] \n{grs}\n{date.today()} \t\t\t\t    {time.strftime("%H:%M")}\n{order}\nPrioritas\t\t\t\t\t1\nSegera Diproses! \n{grs}")
    threading.Thread(target= speak, args= (f"PESANAN BARU DARI OJOL , {item}",), daemon=True).start()

# Generator Walk In
def generator_walkIn():
  menu = ["Kopi Aren", "ButterScotch", "Pasta"]
  while True:
    time.sleep(random.randint(7,7))
    item = random.choice(menu)
    order = Pesanan("WALK-IN", item)

    # Scale Priority = 2
    antrean_utama.put((2, time.time(), order))

    print(f"{grs}\n\t\t[NEW CHECKER] \n{grs}\n{date.today()} \t\t\t\t    {time.strftime("%H:%M")}\n{order}\nPrioritas\t\t\t\t\t2\nSegera Diproses! \n{grs}")
    threading.Thread(target= speak, args= (f"PESANAN BARU WALK-IN, {item}",), daemon=True).start()

# Scheduler
# def scheduler_web():
  while True:
    current_time = time.strftime("%H:%M")
    for order_data in web_schedule_list[:]:
      if order_data["waktu"] == current_time:
        order = Pesanan(order_data["item"], "WEB")

        # Scale Priority = 3
        antrean_utama.put((3, time.time(), order))

        print(f"\n[JADWAL] {order} masuk antrian sesuai jadwal.")
        threading.Thread(target= speak, args= (f"SAATNYA PROSES PESANAN WEB, {order_data["item"]}",), daemon=True).start()
        web_schedule_list.remove(order_data)

    time.sleep(10)


# Thread Pemroses
# TERAKHIR PENGERJAAN STUCK DI NAMA BARISTA
NAMA_BARISTA = ["Ucup", "Asep", "Dadang"]
nama = NAMA_BARISTA
# Ada pembaruan
def barista_eksekutor():
  # Penambahan fitur di barista
  # nama_barista = threading.current_thread().name
  while True:
    if not antrean_utama.empty():
      prio, time_stamp, data = antrean_utama.get()

      print(f"\n >>Barista: { t_barista3.name} SEDANG MEMBUAT: {data} (Prioritas: {prio})  (DURASI: {data.durasi})")
      time.sleep(5)
      print(f">>> Barista:{ t_barista3.name} PESANAN {data} SELESAI!!")

      antrean_utama.task_done()
    if not antrean_utama.empty():

        print(f"\n >>Barista: { t_barista.name} SEDANG MEMBUAT: {data} (Prioritas: {prio})  (DURASI: {data.durasi})")
        pri, time_stamp, data = antrean_utama.get()
        time.sleep(5)
        print(f">>> Barista:{ t_barista.name} PESANAN {data} SELESAI!!")


        antrean_utama.task_done()
      
    else:
      time.sleep(1)

# Main exe
if __name__ == "__main__":
  print("=== SISTEM OTOMASI KAFE DIMULAI ===")
  print("Tekan Ctrl+C untuk berhenti. \n")

# Fitur Nama Barista  
t_barista = threading.Thread(target=barista_eksekutor, name="udin", daemon=True)
t_barista2 = threading.Thread(target=barista_eksekutor, name="Do'eng", daemon=True)
t_barista3 = threading.Thread(target=barista_eksekutor, name="Asep", daemon=True)
# Inisialisasi thread
t_ojol = threading.Thread(target=generator_ojol, daemon=True)
t_walkin = threading.Thread(target=generator_walkIn, daemon=True)
# t_web = threading.Thread(target=scheduler_web, daemon=True)
# Penambahan Jumlah Barista
t_ojol.start()
t_walkin.start()
# t_web.start()
t_barista.start()
t_barista2.start()
t_barista3.start()


try: 
  while True:
    time.sleep(1)
except KeyboardInterrupt:
  print("\n Sistem dimatikan oleh user")

