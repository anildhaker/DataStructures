class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        

class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def printlList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next 

    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
        

    def delLinkList(self):
      curr = self.head
      
      while (curr):
          temp = curr.next
          
          del curr.data
          
          curr = temp
        
llist = LinkedList() 
llist.push(7) 
llist.push(1) 
llist.push(3) 
llist.push(2) 
llist.push(8)


print("before deletion --")
llist.printlList()

llist.delLinkList()
print("Link List deleted")
