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
    
    def eleFreq(self, element):
      current = self.head
      count = 0

      while (current is not None):
        if current.data == element:
          count += 1
        current = current.next
      return count
    

if __name__=='__main__': 
    llist = LinkedList() 
    llist.push(1) 
    llist.push(3) 
    llist.push(1) 
    llist.push(2) 
    llist.push(1)

    print(llist.eleFreq(1))