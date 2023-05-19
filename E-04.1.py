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
'''

Ejercicio : Calcular la suma del siguiente 
            arbol generico

           17
       /   |  \
     /     |    \
    3       4     5 
  / | \     |
 3  4  5    10 

'''

if __name__ == '__main__':

    nodeA = TreeNode(17)
    nodeB = TreeNode(3)
    nodeC = TreeNode(4)
    nodeD = TreeNode(5)
    nodeE = TreeNode(3)
    nodeG = TreeNode(4)
    nodeH = TreeNode(5)
    nodeI = TreeNode(10)

    nodeA.firstChild = nodeB
    nodeB.firstChild = nodeE
    nodeE.nextSibling = nodeG
    nodeG.nextSibling = nodeH
    nodeB.nextSibling = nodeC
    nodeC.firstChild = nodeI
    nodeC.nextSibling = nodeD

    # Suma
    print(findSum(nodeA))

