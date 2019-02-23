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

    def printList(self):  
        temp = self.head  
        while(temp):  
            print(temp.data ) 
            temp = temp.next
            
    def removeNode(self, node):
      temp = self.head

      while temp is not None:
        if temp == node:
          break
        prev = temp
        temp = temp.next
      if temp == None:
        return

      prev.next = temp.next
      temp = None

        

    def removeDuplicates(self,llist):
      current1 = self.head
      while (current1):
        data = current1.data
        current2 = current1.next
        while (current2):
          if current2.data == data:
            llist.removeNode(current2)
          current2 = current2.next
        current1 = current1.next



llist = LinkedList() # Here we are working with Unsorted linked List
llist.push(1) 
llist.push(3) 
llist.push(2) 
llist.push(4)
llist.push(2)
llist.push(4)
llist.push(3)

llist.printList()
llist.removeDuplicates(llist)
print()
llist.printList()
print()