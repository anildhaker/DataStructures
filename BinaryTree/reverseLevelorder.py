class Stack(object):
  def __init__(self):
    self.items = []

  def push(self,item):
    self.items.append(item)

  def Pop(self):
    if not self.is_empty():
      return self.items.pop()

  def is_empty(self):
    return len(self.items) == 0

  def peek(self):
    if not self.is_empty():
      return self.items[-1]

  def __len__(self):
    return self.size()

  def size(self):
    return len(self.items)

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

  
  def reverse_level_traversal(self, start):
    if start is None:
      return

    stack = Stack()
    queue = Queue()

    queue.enQueue(start)

    traversal = ''

    while len(queue) > 0:
      node = queue.deQueue()
      stack.push(node)

      if node.right:
        queue.enQueue(node.right)

      if node.left:
        queue.enQueue(node.left)
    while len(stack) > 0:
      node = stack.Pop()
      traversal += str(node.data) + " "
    return traversal
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.reverse_level_traversal(tree.root))