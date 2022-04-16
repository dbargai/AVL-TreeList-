def isAVL(node):
    if node.getHeight()==-1:
        return True
    l=isAVL(node.left)
    if abs(node.getBF())>1:
        return False
    r=isAVL(node.right)
    
    return l and r 


##### Add this to Node Class: ######
def getBF(self):
    return self.getLeft().getHeight() - self.getRight().getHeight()
