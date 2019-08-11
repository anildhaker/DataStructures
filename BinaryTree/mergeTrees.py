# Giventwobinarytrees and imaginethatwhenyouputoneofthemtocover
# the other, some nodes of the two trees are overlapped while the others are not.

# Youneedtomergethemintoanewbinarytree.Themergerule is that if two
# nodesoverlap, thensumnodevaluesup as thenewvalueofthemergednode.
# Otherwise, the NOT null node will be used as the node of new tree.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
      if not t1 and not t2:
          return None 
      ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
      ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
      ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
      return ans