import queue
import threading
import time
import random
import pyttsx3
import os

os.system("cls")

#Insialisasi Pesan orderan
text = "PT. JayaSukses \t 0888 1132 2234 \t Raya Kutabaru"
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
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()
  except:
    pass

# Class Pesanan
class Pesanan:

  def __init__(self, nama, asal):
    self.nama = nama
    self.asal = asal

  def __repr__(self):
    return f"[{self.asal}] {self.nama}"

# fungsi thread ojol
def generator_ojol():
  menu = ["Kopi Kampung", "Blue Lagon", "MilkTea"]
  while True:
    time.sleep(random.randint(7, 12))
    item = random.choice(menu)
    order = Pesanan(item, "OJOL")

    # Priority 1 Ojol
    antrean_utama.put((1, time.time(), order))

    print(f"===================\n[NEW CHECKER] \n====================\n {order} \n====================\n - Segera diproses!")
    threading.Thread(target= speak, args= (f"PESANAN BARU , {item}",), daemon=True).start()

# Generator Walk In
def generator_walkIn():
  menu = ["Kopi Aren", "ButterScotch", "Pasta"]
  while True:
    time.sleep(random.randint(15, 20))
    item = random.choice(menu)
    order = Pesanan(item, "WALK-IN")

    # Scale Priority = 2
    antrean_utama.put((2, time.time(), order))

    print(f"\n [MASUK] {order}")
    threading.Thread(target= speak, args= (f"PESANAN BARU, {item}",), daemon=True).start()

# Scheduler
def scheduler_web():
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
def barista_eksekutor():
  while True:
    if not antrean_utama.empty():
      prio, time_stamp, data = antrean_utama.get()

      print(f"\n >>Barista: Membuat {data} (Prioritas: {prio})")
      time.sleep(5)
      print(f">>> Barista: {data} SELESAI!!")

      antrean_utama.task_done()
    else:
      time.sleep(1)

# Main exe
if __name__ == "__main__":
  print("=== SISTEM OTOMASI KAFE DIMULAI ===")
  print("Tekan Ctrl+C untuk berhenti. \n")


# Inisialisasi thread
t_ojol = threading.Thread(target=generator_ojol, daemon=True)
t_walkin = threading.Thread(target=generator_walkIn, daemon=True)
t_web = threading.Thread(target=scheduler_web, daemon=True)
t_barista = threading.Thread(target=barista_eksekutor, daemon=True)

t_ojol.start()
t_walkin.start()
t_web.start()
t_barista.start()


try: 
  while True:
    time.sleep(1)
except KeyboardInterrupt:
  print("\n Sistem dimatikan oleh user")