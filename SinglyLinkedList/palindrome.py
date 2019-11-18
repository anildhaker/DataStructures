# Check if link list is palindrome

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None 

class LinkedList: 
  
    def __init__(self): 
        self.head = None
    
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node

# Using a stack -- traverse link list - put in stack.
# Traverse once again and pop from stack to compare. 
    def isPalindrome(self):
      s = []
      temp = self.head
      while temp:
        s.append(temp.data)
        temp = temp.next

      print(s)
        
      temp1 = self.head
      while temp1:
        if s.pop() == temp1.data:
          temp1 = temp1.next
        else:
          return False
      return True 

        

llist = LinkedList() 
llist.push(1) 
llist.push(2) 
llist.push(1) 
llist.push(2) 
llist.push(1)


print(llist.isPalindrome())