# Approach - reverse the second half of the list. Compare with first half.
# Reverse it again to get original linked list.

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

    def midNode(self):
      slow = self.head
      fast = self.head
      
      while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        
      return slow

    def printlList(self):
        temp = self.head
        while (temp):
          print(temp.data)
          temp = temp.next 

    def reverseLinkList(self):
      prev = None
      curr = self.head
      nxt = None
      
      while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
      
      self.head = prev

    def isPalindrome(self):
      SecondHalf = self.midNode()
      pass 
      
        
llist = LinkedList() 
llist.push(1) 
llist.push(2) 
llist.push(1) 
llist.push(20) 
llist.push(10)

print("Link list before reversal")
llist.printlList()
# print("After reversal--")
# llist.reverseLinkList()
# llist.printlList()

llist.isPalindrome()


