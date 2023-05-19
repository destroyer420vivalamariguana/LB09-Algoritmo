class BinaryTreeNode:

    def __init__(self, data, left = None, right = None):
        self.data = data  # value node
        self.left = left  # left child
        self.right = right # right child

def proRecursive(root):
    if (root == None):
        return 1
    return root.data * \
           proRecursive(root.left) * \
           proRecursive(root.right)

#
# Resolution
#           1
#       2       3
#     7   5   6   7

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(7)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)

tmp = proRecursive(root)
print("El producto de los nodos del arbol es %d" % (tmp))
