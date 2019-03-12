class Queue():
  def __init__(self):
    self.inStack = []
    self.outStack = []

  def enQueue(self,e):
    self.inStack.append(e)

  def deQueue(self):
    if not self.outStack:
      while self.inStack:
        self.outStack.append(self.inStack.pop())
    return self.outStack.pop()

q = Queue()  

for i in range(1, 11):
  q.enQueue(i)



print

for i in range(10):
  print (q.deQueue())

#StackPrint



    

