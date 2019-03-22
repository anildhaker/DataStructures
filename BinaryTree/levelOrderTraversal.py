# Use Queue data structure
class Queue(object):
  def __init__(self):
    self.items = []

  def enQueue(self,item):
    self.items.insert(0, item)
    
  def deQueue(self):
    if not self.is_empty():
      return self.items.pop()

  def is_empty(self):
    return len(self.items) == 0
    
  def peek(self):
    if not self.is_empty():
      return self.items[-1].data

  def __len__(self):
    return self.size()

  def size(self):
    return len(self.items)

    
class Node(object):
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    
class BinaryTree(object):
  def __init__(self, root):
    self.root = Node(root)
  
  def level_Order_travelsal(self,start):
    if start is None:
      return
    
    queue = Queue()
    queue.enQueue(start)

    traversal = ""

    while len(queue) > 0:
      traversal += str(queue.peek()) + " "
      node = queue.deQueue()

      if node.left:
        queue.enQueue(node.left)

      if node.right:
        queue.enQueue(node.right)

    return traversal
  
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(tree.level_Order_travelsal(tree.root))