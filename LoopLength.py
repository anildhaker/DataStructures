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

    def append(self, new_data):
      if self.head == None:
        self.head = Node(new_data)
      
      current = self.head
      while (current.next):
        current = current.next
      current.next = Node(new_data)

    def createLoop(self, index):
      intersection = self.head

      for i in range(1, index):
        intersection = intersection.next

      end = self.head
      while (end.next):
        end = end.next
      
      end.next = intersection

    def loopLength(self):
      if self.head is None:
        return 0

      slow = self.head
      fast = self.head
      flag = 0
      
      while (slow and slow.next and fast and fast.next and fast.next.next):
        
        if (slow == fast and flag != 0):
          count = 0
          slow = slow.next
          while (slow != fast):
            slow = slow.next
            count += 1
          return count
        
        slow = slow.next
        fast = fast.next.next
        flag = 1
      return 0
        

if __name__=='__main__': 
    llist = LinkedList() 
    llist.append(1) 
    llist.append(2) 
    llist.append(3) 
    llist.append(4)
    llist.append(5)

    llist.createLoop(2)

    loop_length = llist.loopLength()
    print(loop_length)
