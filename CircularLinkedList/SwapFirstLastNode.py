class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
  
class CircularLinkedList:
  
    def __init__(self): 
        self.head = None
  
    #insert Node at beginning
    def push(self, data): 
        new_node = Node(data) 
        temp = self.head 
          
        new_node.next = self.head 
  
        # If linked list is not None then set the next of 
        # last node 
        if self.head is not None: 
            while(temp.next != self.head): 
                temp = temp.next 
            temp.next = new_node 
  
        else: 
            new_node.next = new_node # For the first node 
  
        self.head = new_node  
  
 
    def printList(self): 
        temp = self.head 
        if self.head is not None: 
            while(True): 
                print ("%d" %(temp.data),)
                temp = temp.next
                if (temp == self.head): 
                    break

    def remove_node(self, node):
        if self.head == node:
            cur = self.head 
            while cur.next != self.head:
                cur = cur.next 
            cur.next = self.head.next 
            self.head = self.head.next
        else:
            cur = self.head 
            prev = None
            while cur.next != self.head:
                prev = cur 
                cur = cur.next 
                if cur == node:
                    prev.next = cur.next
                    cur = cur.next
        

    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count

    def swapFirstLastNode(self):
      prev = None
      cur = self.head

      while (cur.next != self.head):
        prev = cur
        cur = cur.next
      prev.next = self.head
      cur.next = self.head.next
      self.head.next = cur
      self.head = cur

cllist = CircularLinkedList() 
  
cllist.push(40) 
cllist.push(30) 
cllist.push(20) 
cllist.push(10)

cllist.printList()
print
cllist.swapFirstLastNode()
cllist.printList()