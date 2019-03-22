class Node(object):
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    

class BinaryTree(object):
  def __init__(self, root):
    self.root = Node(root)

  def height(self, node):
    if node is None:
      return - 1
    
    left_height = self.height(node.left)
    right_height = self.height(node.right)
    return 1 + max(left_height,right_height)


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.left = Node(8)


print(tree.height(tree.root))

  