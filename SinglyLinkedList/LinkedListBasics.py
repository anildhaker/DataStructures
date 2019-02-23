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
    
    def push(self,new_data):
        
        new_Node = Node(new_data)
        
        new_Node.next = self.head
        
        self.head = new_Node
    
    def insertAfter(self,prev_node,new_data):
        
        new_Node = Node(new_data)
        
        new_Node.next = prev_node.next
        prev_node.next = new_Node
        
    def append(self,new_data):
        
        new_Node = Node(new_data)
        
        temp = self.head
        while(temp.next):
            temp = temp.next
        
        temp.next = new_Node
        
    def deleteNode(self, key):
        
        temp = self.head
        
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return 
        
        while(temp is not None):
            if (temp.data == key):
                break
            prev = temp 
            temp = temp.next
        
        if temp == None:
            return 
        
        prev.next = temp.next
        temp = None
        
    def delNodePosition(self,position):
        if self.head == None:
            return
        
        temp = self.head
        
        if position == 0:
            self.head = temp.next
            temp = None
            return 
        
        #finding previous node- 
        
        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        
        nex = temp.next.next
        temp.next = None
        temp.next = nex
            
        
              
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