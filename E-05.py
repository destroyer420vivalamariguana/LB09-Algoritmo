class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def eval(self):

        if self.right is not None and self.left is not None:
            if self.value == '+':
                return self.left.eval() + self.right.eval()
            elif self.value == '*':
                return self.left.eval() * self.right.eval()
        else:
            return float(self.value)

#################################
# First Case : ((2 + 4) * 2 + 5)
#
#         *
#     +      +
#   2   4  2   5
#################################
def evalManual():

    opeNodeA = Node(2)
    opeNodeB = Node(4)

    opeNodeC = Node(2)
    opeNodeD = Node(5)

    sumNodeL = Node('+')
    sumNodeL.left = opeNodeA
    sumNodeL.right = opeNodeB

    sumNodeR = Node('+')
    sumNodeR.left = opeNodeC
    sumNodeR.right = opeNodeD

    mulNode = Node('*')
    mulNode.left = sumNodeL
    mulNode.right = sumNodeR

    print(mulNode.eval())

#################################
# Main
#################################
if __name__ == '__main__':
    '''
    Este metodo es para 
    '''
    evalManual()
    # evalPostfixExpression()
    # convertIndorToPostfixExp()
    # evalIndorExpression()

