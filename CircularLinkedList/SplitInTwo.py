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
  
    # Function to print nodes in a given circular linked list 
    def printList(self): 
        temp = self.head 
        if self.head is not None: 
            while(True): 
                print "%d" %(temp.data), 
                temp = temp.next
                if (temp == self.head): 
                    break
                    
    def splitList(self, head1, head2):
      slow = self.head
      fast = self.head

      if self.head is None:
        return

      while (fast.next != self.head and fast.next.next != self.head):
        slow = slow.next
        fast = fast.next.next

      if fast.next.next == self.head: #Tackling case for even nodes
        fast = fast.next
      
      head1.head = self.head

      if self.head.next != self.head:
        head2.head = slow.next

      fast.next = slow.next  # making second list circular

      slow.next = self.head # making second list circular


cllist = CircularLinkedList()
head1 = CircularLinkedList()
head2 = CircularLinkedList()

  
# Created linked list will be 11->2->56->12 
cllist.push(12) 
cllist.push(56) 
cllist.push(2) 
cllist.push(11) 
  
print "Contents of circular Linked List"
cllist.printList()
cllist.splitList(head1,head2)
print
head1.printList()
print
head2.printList()