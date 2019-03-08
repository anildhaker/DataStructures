class KStacks:
  def __init__(self, k, n):
    self.k = k  #number of stacks
    self.n = n  #arrayLength

    self.arr = [0] * self.n    # main Array which will store all K stacks
    self.top = [-1] * self.k  # Creating array for top of all K stacks
    
    self.free = 0  #Top of Free Slots

    self.next = [i + 1 for i in range(self.n)] 
    self.next[self.n - 1] = -1

  
  def is_empty(self, sn):
    return self.top[sn] == -1

  def is_Full(self):
    return self.free == -1

  
  #push element in a given Stack number
  
  def push(self,item, sn):
    if self.is_Full():
      print('Stack OverFlow')
      return
    
    free_pos = self.free
    self.free = self.next[self.free] 
    self.arr[free_pos] = item
    
    self.top[sn] = free_pos

  def pop(self, sn): 
        if self.isEmpty(sn): 
            return None
  
        # Get the item at the top of the stack. 
        top_of_stack = self.top[sn] 
  
        # Set new top of stack. 
        self.top[sn] = self.next[self.top[sn]] 
  
        # Push the old top_of_stack to  
        # the 'free' stack. 
        self.next[top_of_stack] = self.free 
        self.free = top_of_stack 
  
        return self.arr[top_of_stack] 




  
   