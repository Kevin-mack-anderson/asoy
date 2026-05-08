

# # # Stack

# # data = [1,2,3,4,5,6,7]
# # print(f"Data sekarang {data}")
# # data.append(8)
# # print(f"Data Sekarang: {data}")

# # # Out
# # out = data.pop()
# # print(f"Data Keluar {out}")
# # print(f"Data Sekarang {data}")

# # # Queue
# # from collections import deque

# # data_2 = deque([1,2,3,4,5,6])
# # print(f"Data Sekarang : {data_2}")
# # data_2.append(7)
# # print(f"Data Sekarang {data_2}")

# # # out
# # out_2 = data_2.popleft()
# # print(f"Data keluar {out_2}")
# # print(f"Data Sekarang {data_2}")




# # LAgi

# stack = []

# def push(value):
#   stack.append(value)

# def pop(value):
#   stack.pop(value)
  
# def noel():
#   print(len(stack))

# def top():
#   top = len(stack) - 1 
#   if top < 0:
#     print("Tidak Terdefinisi")
#   else:
#     print(stack[top])

# def isEmpty():
#   if len(stack) == 0:
#     print("True")
#   else:
#     print("False")

# def tampilkan(stack):
#   print(stack)

# # antrian = input("Antrian B-2")
# # Agar gampang digunakan

# while True:
#   print(f"Data Stack Saat Ini = {stack}")
#   print(" 1.Push||2.Pop \n 3.noel||4.Top \n 5.IsEmpty ")
#   pilihan = str(input("Masukan Metode : "))

#   if pilihan == "1":
#     psh = str(input("Masukan String : "))
#     push(psh)
#     print(f"Data Yang Dimasukan [{psh}], Stack Saat Ini {stack}")
#   elif pilihan == "2":
#     pp = int(input("Berapa Data Yang Ingin Dihapus : "))
#     pop(pp)
#     print(f"Data Yang Di Pop [{pp}], Stack Saat Ini {stack}")
#   elif pilihan == "3":
#     print(f"Panjang Stack Adalah = {noel()}")
#   elif pilihan == "4":
#     print(f"Nilai Puncak [{top()}]")
#   elif pilihan == "5":
#     print(isEmpty())
#   else:
#     print("SEPERTINYA ADA YANG SALAH DEH")
    

# QUEUE

Node = []

def __init__(self):
   self.head = Node("head")
   self.size = 0

def isEmpty(self):
   return self.size == -1

def peek(self):
   if self.isEmpty():
    raise Exception("Peeking from an empty stack")
    return self.head.next.value
  
def enqueue(self, value):
   node = Node(value)
   node.next = self.head.next
   self.head.next = node
   self.size += 1

def dequeue(self):
   if self.isEmpty():
    raise Exception("dequeue from an empty stack")
   remove = self.head.next
   self.head.next = self.head.next.next
   self.size -= 1
   return remove.value

def getSize(self):
   return self.size
print(enqueue())



