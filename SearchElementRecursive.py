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

    def search(self, node, key):
      if not node:
        return False
      
      if node.data == key:
        return True
      else:
        return self.search(node.next,key)

if __name__=='__main__': 
    llist = LinkedList() 
    llist.push(1) 
    llist.push(3) 
    llist.push(1) 
    llist.push(2) 
    llist.push(1) 
    print (llist.search(llist.head,21))  # Returns false