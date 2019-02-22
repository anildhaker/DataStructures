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

    def count(self, lst, element):

      if not lst:
        return self.counter
      
      if (lst.data == element):
        self.counter = self.counter + 1
      return self.count(lst.next,element)
      

if __name__=='__main__': 
    llist = LinkedList() 
    llist.push(1) 
    llist.push(3) 
    llist.push(1) 
    llist.push(2) 
    llist.push(1)

    print(llist.count(llist.head,1))