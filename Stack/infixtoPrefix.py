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
      return char.isalpha()

    # check the precedence of operator --> is it strictly lesser than 

    def notGreater(self, i):
      a = self.precedence[i]
      b = self.precedence[self.peek()]
      return True if a <= b else False


    def reverseExp(self, exp):
      reversedExp = exp[::-1]
      list_reverse_exp = list(reversedExp)

      for i, c in enumerate(list_reverse_exp):
            if list_reverse_exp[i] == '(':
                list_reverse_exp[i] = ')'
            elif list_reverse_exp[i] == ')':
                list_reverse_exp[i] = '('
      s = ''.join(list_reverse_exp)
      return s

    def infixToPrefix(self, exp):
        reversed_exp = self.reverse(exp)
        for i in reversed_exp:
            if self.isOperand(i):
                self.output.append(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                while not self.isEmpty() and self.peek() != '(':
                    a = self.pop()
                    self.output.append(a)
                if not self.isEmpty() and self.peek() != '(':
                    return -1
                else:
                    self.pop()
            else:
                while not self.isEmpty() and self.notGreater(i):
                    self.output.append(self.pop())
                self.push(i)
        while not self.isEmpty():
            self.output.append(self.pop())
        temp = "".join(self.output)
        infix_to_prefix_expression = self.reverse(temp)
        print(infix_to_prefix_expression)
      



      

    

