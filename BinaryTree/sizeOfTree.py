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


class Node(object):
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinaryTree(object):
  def __init__(self, root):
    self.root = Node(root)
   
  def size_of_tree(self):
    if self.root is None:
      return 0

    stack = Stack()
    stack.push(self.root)
    size = 1
    while len(stack) > 0:
      node = stack.Pop()

      if node.left:
        size += 1
        stack.push(node.left)

      if node.right:
        size += 1
        stack.push(node.right)
    return size
      
  


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)


print(tree.size_of_tree())