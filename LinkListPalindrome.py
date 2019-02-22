class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None 
  
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.counter = 0
  

    def push(self, new_data): 
  
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
      
    def isPalindrome(self):
      temp = []

      current = self.head
      while (current is not None):
        temp.append(str(current.data))
        current = current.next
      string = ''.join(temp)
      result = (string == string[::-1])

      return result

llist = LinkedList() 
llist.push(1) 
llist.push(2) 
llist.push(2) 
llist.push(1)

print(llist.isPalindrome())