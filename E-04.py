########################################
#       Generic Tree
########################################
class TreeNode:

    #Constructor
    def __init__(self, data=None):
        self.data = data
        self.firstChild = None
        self.nextSibling = None

def findSum(root):
    if(root == None):
        return 0
    return root.data + \
        findSum(root.firstChild) + \
        findSum(root.nextSibling)

# programa principal
#
#           A,1
#    /  \    \       \
#   |    |    |       |
#  B,2  C,3    D,4   E,10
#        |      |
#        |      |
#       G,20   H,15
#
if __name__ == '__main__':

    nodeA = TreeNode(1)
    nodeB = TreeNode(2)
    nodeC = TreeNode(3)
    nodeD = TreeNode(4)
    nodeE = TreeNode(10)
    nodeG = TreeNode(20)
    nodeH = TreeNode(15)

    nodeA.firstChild = nodeB
    nodeB.nextSibling = nodeC
    nodeC.nextSibling = nodeD
    nodeC.firstChild = nodeG
    nodeD.nextSibling = nodeE # Defino su hermano
    nodeD.firstChild = nodeH  # Defino un hijo

    # Suma
    print(findSum(nodeA))
