class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        

class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
    

    def delLinkList(self):
      current = self.head
      
      while (current):
        prev = current.next

        del (current.data)
        
        current = prev
            
        
              
if __name__=='__main__':
    
    llist = LinkedList()
    
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    llist.head.next = second 
    second.next = third
    
    llist.push(5)
    llist.append(6)
    
    llist.printList()
    llist.delNodePosition(2)
    print()
    llist.printList()