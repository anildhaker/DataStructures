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

    def detectLoop(self):
      s = set()
      temp = self.head
      while (temp):
        if (temp in s):
          return True
        s.add(temp)
        temp = temp.next
      return False


if __name__=='__main__': 
    llist = LinkedList() 
    llist.push(1) 
    llist.push(3) 
    llist.push(1) 
    llist.push(2)
    
    llist.head.next.next.next.next = llist.head;

    print(llist.detectLoop())