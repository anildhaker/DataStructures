# check if parentheses are balanced or not ?

def balanced_parantheses(str):
    stack = []

    for i in range(len(str)):
        char = (str[i])

        if char == "(" or char == "[" or char == "{":
            stack.append(char)

        elif char == ")" or char == "]" or char == "}":
            if (len(stack) == 0): 
                return "Not Balanced"
            else: 
                bracket = stack.pop()
                if bracket == "(" and char != ")":
                    return "Not Balanced"
                elif bracket == "{" and char != "}":
                    return "Not Balanced"
                elif bracket == "[" and char != "]":
                    return "Not Balanced"           

    if  len(stack) == 0:
        return "Balanced"
    else:
        return "Not Balanced"
        


  
string  = '[{(a+b) * (c/d)}]'
print(balanced_parantheses(string))

