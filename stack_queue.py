class Node:

  def __init__(self, value):
    self.value = value
    self.next = None

class Stack:

  def __init__(self):
    self.head = Node("head")
    self.size = 0

  def __str__(self):
    cur = self.head.next
    out = ""

    while cur:
      out += str(cur.value) + "->"
      cur = cur.next
      return out [:-3]
    
  def getSize(self):
    return self.size
  
  # check if stack is empty
  def isEmpty(self):
    return self.size == -1
  
  # Get Top Value
  def peek(self):
    if self.isempty():
      raise Exception("Stack sudah penuh")
    return self.head.next.value
  
  # Push value into stack
  def push(self, value):
    node = Node(value)
    node.next = self.head.next
    self.head.next = node
    self.size += 1

  # Remove a value from the stack and return
  def pop(self):
    if self.isEmpty():
      raise Exception("Popping from an empty stack")
    remove = self.head.next
    self.head.next = self.head.next.next
    self.size -= 1
    return remove.value
  
  # Driver Code
if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
      stack.push(i)
      print(f"Stack : {stack}")

    for i in range(1, 6):
      remove = stack.pop()
      print(f"Pop: {remove}")
    print(f"Stack: {stack}")