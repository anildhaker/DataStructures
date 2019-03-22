class Node(object):
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    

class BinaryTree(object):
  def __init__(self, root):
    self.root = Node(root)

  def print_tree(self, traversal_type):
    if traversal_type == "preorder":
      return self.pre_order_print(tree.root, "")
      
    elif traversal_type == "inorder":
      return self.in_order_print(tree.root, "")

    elif traversal_type == "postorder":
      return self.post_order_print(tree.root,"")  

    else:
      print("Traversal type --> " + traversal_type + " is not supported")
      return False


  # pre order Traversal
  def pre_order_print(self, start, traversal):
    # Root --> left --> right
    if start:
      traversal += (str(start.data) + " ")
      traversal = self.pre_order_print(start.left, traversal)
      traversal = self.pre_order_print(start.right, traversal)
    return traversal


  def in_order_print(self, start, traversal):
    # Left --> Root --> right
    if start:
      traversal = self.in_order_print(start.left, traversal)
      traversal += str(start.data) + " "
      traversal = self.in_order_print(start.right, traversal)
      
    return traversal

  def post_order_print(self, start, traversal):
    # Left --> Right --> Root
    if start:
      traversal = self.post_order_print(start.left, traversal)
      traversal = self.post_order_print(start.right, traversal)
      traversal += str(start.data) + " "
    return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)


print(tree.print_tree("postorder"))



