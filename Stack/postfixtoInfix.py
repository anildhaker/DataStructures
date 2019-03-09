def postfixto_Infix(expression):
  l = len(expression)

  output = []

  for i in range(l):
    if expression[i].isalpha():
      output.append(expression[i])
    else:
      operand1 = output.pop()
      operand2 = output.pop()
      operator = expression[i]
      expression = '(' + operand2 + operator + operand1 + ')'
      output.append(expression)

  return output

data = "ab*c+"
print(postfixto_Infix(data))
