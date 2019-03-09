# Infix to prefix Python Implementation

class Conversion:
    def __init__(self, capacity):
      self.capacity = capacity
      self.top = -1

      self.array = []
      self.output = []

      self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
      

    def isEmpty(self):
      return True if self.top == -1 else False

    def peek(self):
      return self.array[-1]

    def pop(self):
      if not self.isEmpty():
        self.top -= 1
        return self.array.pop()

      else:
        print('Nothing to Pop')
    
    def push(self,data):
      self.top += 1
      return self.array.append(data)

    
    def is_Operand(self, char):
      

    

