class TwoStacksInArray():
  def __init__(self, n):
    self.size = n
    self.arr = [None]*n
    self.top1 = -1
    self.top2 = self.size

  
  def push1(self, x):
    if self.top1 < self.top2 - 1:
      self.top1 += 1
      self.arr[self.top1] = x

    else:
      print('Stack OverFlow')

  
  def push2(self, x):
    if self.top1 < self.top2 - 1:
      self.top2 -= 1
      self.arr[self.top2] = x
    else:
      print('Stack OverFlow')

  def pop1(self):
    if self.top1 >= 0:
      x = self.arr[self.top1]
      self.top1 -= 1
      return x
    else:
      print("stack underFlow")

  def pop2(self):
    if self.top2 >= 0:
      x = self.arr[self.top2]
      self.top1 += 1
      return x
    else:
      print("stack underFlow")


#Code Driver

stacks = TwoStacksInArray(5)
stacks.push1(4)
stacks.push2(41)
stacks.push2(114)
stacks.push1(4444)
stacks.push2(4342)

print(stacks.pop1())
print(stacks.pop2())




  
      

  