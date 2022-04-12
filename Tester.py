import unittest
import avl_skeleton as AVLTreeList
import math
import random


def printTreefinal(tree):
    out = ""
    for row in printree(tree.getRoot()):  # need printree.py file
        out = out + row + "\n"
    print(out)
"""returns index of given node in the list
!!! This method is for testing and does not run on O(1), don't use for class methods
"""
def printree(t, bykey=True):
    """Print a textual representation of t
    bykey=True: show keys instead of values"""
    # for row in trepr(t, bykey):
    #        print(row)
    return trepr(t, bykey)


def trepr(t, bykey=False):
    """Return a list of textual representations of the levels in t
    bykey=True: show keys instead of values"""
    if t.getSize() == 0:
        return ["#"]

    thistr = str(t.getValue()) if bykey else str(t.getValue())

    return conc(trepr(t.left, bykey), thistr, trepr(t.right, bykey))


def conc(left, root, right):
    """Return a concatenation of textual represantations of
    a root node, its left node, and its right node
    root is a string, and left and right are lists of strings"""

    lwid = len(left[-1])
    rwid = len(right[-1])
    rootwid = len(root)

    result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

    ls = leftspace(left[0])
    rs = rightspace(right[0])
    result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid * " " + "\\" + rs * "_" + (rwid - rs) * " ")

    for i in range(max(len(left), len(right))):
        row = ""
        if i < len(left):
            row += left[i]
        else:
            row += lwid * " "

        row += (rootwid + 2) * " "

        if i < len(right):
            row += right[i]
        else:
            row += rwid * " "

        result.append(row)

    return result


def leftspace(row):
    """helper for conc"""
    # row is the first row of a left node
    # returns the index of where the second whitespace starts
    i = len(row) - 1
    while row[i] == " ":
        i -= 1
    return i + 1


def rightspace(row):
    """helper for conc"""
    # row is the first row of a right node
    # returns the index of where the first whitespace ends
    i = 0
    while row[i] == " ":
        i += 1
    return i


def indexOf(node):
    parent = node
    if parent.getParent().getLeft() is parent:
        while parent.getParent().getLeft() is parent:
            parent=parent.getParent()
        return node.getLeft().getSize()+parent.getLeft()+1
    else:
        while parent.getParent().getroght is parent:
            parent = parent.getParent()
        return node.getParent().getLeft().getSize()+1+parent.getLeft().getSize()+1 + node.getLeft.getSize()


def isAVL(node):
    if node.getHeight()==-1:
        return True
    l=isAVL(node.left)
    if abs(node.getBF())>1:
        return False
    r=isAVL(node.right)
    
    return l and r 

def setFirst(tree):
    first=tree.getRoot()
    while first.getLeft().isRealNode():
        first = first.getLeft()
    tree.firstitem = first

def setLast(tree):
    last=tree.getRoot()
    while last.getRight().isRealNode():
        last = last.getRight()
    tree.lastitem = last

"""This method is for testing ONLY and returns a legal tree basded in a given list
@pre: list of strings which satisfies the following format: (examples ahead)
	list length is a power of 2 minus 1 and
	index 0 is the root
    next 2 indexes are the sons of the root,
	next 4 indexes are the sons of the root's sons, from left to right
    next 8 ...
	and so on by this pattern while a "missing son" will be represented by None
@post: False if list represents illegal tree, compatible AVLTreeList otherwise
@rtype: AVLTreeList

examples:
The list ['a','b','c','d','e',None,'f'] will create the following tree
(including virtual sons which are not detailed here)
             a
          /     \
        b         c
      /   \         \
     d     e         f

The list ['a','None','c',None, None, None, 'f'] will return False 
because it represents an illegal tree:
             a
                \
                  c
                    \
                     f
"""

def createTreeFromList(lst):
    if len(lst)==0:
        return AVLTreeList.AVLTreeList()
    x= math.log(len(lst), 2)
    y = x%1
    if math.log(len(lst) +1, 2)%1!=0:
        return False
    tree = AVLTreeList.AVLTreeList()
    root = createTreeFromList_rec(lst,0,0)
    if root.height>-2:
        tree.root=root
        setFirst(tree)
        setLast(tree)
        return tree
        
    else:
        print("list does not represent a valid tree")
        return False

def createTreeFromList_rec(lst, i, power):
    if(lst[i]==None):
		#return virtual Node from lst[i]:
        return AVLTreeList.AVLNode(lst[i])

	##calc next index of left son's index, right son will be the following index:
    nextIndex=i+2**power+(i+1)-2**(math.floor(math.log(i+1,2)))
    
    if nextIndex>=len(lst):
        node = AVLTreeList.AVLNode(None)
        node.setFields(lst[i], AVLTreeList.AVLNode(None), AVLTreeList.AVLNode(None), None, 0, 1)
        node.getLeft().setParent(node)
        node.getRight().setParent(node)
        return node

    left = createTreeFromList_rec(lst, nextIndex, power+1)
    right = createTreeFromList_rec(lst, nextIndex +1, power+1)
    if left.getHeight()>-2 and right.getHeight()>-2:
        if abs(right.height-left.height)>1:
            node = AVLTreeList.AVLNode(None)
            node.setHeight(-2)
            return node

        else:
            node = AVLTreeList.AVLNode(lst[i])
            node.setFields(lst[i], left, right, None, max(left.getHeight(), right.getHeight()) +1, left.getSize()+right.getSize()+1)
            left.setParent(node)
            right.setParent(node)
            return node

    else:
        node = AVLTreeList.AVLNode(None)
        node.setHeight(-2)
        return node

""" returns true if trees are totally equal, false if not
    comparison between all fields of each node and all fields of the tree itself
"""
def compareTrees(tree1, tree2):
    if compareNodes(tree1.firstitem,tree2.firstitem) and compareNodes(tree1.lastitem,tree2.lastitem):
        return compareTreesRec(tree1.getRoot(), tree2.getRoot())
    return False
    
def compareTreesRec(root1, root2):
    if not root1.isRealNode() or not root2.isRealNode():
        return compareNodes(root1, root2)
    if not compareTreesRec(root1.getLeft(), root2.getLeft()):
        return False
    elif not compareNodes(root1, root2):
        return False
    elif not compareTreesRec(root1.getRight(), root2.getRight()):
        return False
    return True


""" return true if 2 nodes are equal by size, height, value
@pre: root1 and root2 are AVLNodes types
"""
def compareNodes(node1, node2):
    return node1.getSize()==node2.getSize() and \
            node1.getValue()==node2.getValue() and \
            node1.getHeight() == node2.getHeight()
                    


class TestMavnatProject1(unittest.TestCase):

    def testCompareTrees(self):
        # Fix AVLTreeList constructor before activating this test:
        # tree1 = createTreeFromList([])
        # tree2 = createTreeFromList([])
        # self.assertEqual(compareTrees(tree1, tree2), True)

        tree1 = createTreeFromList(["a","b","c","d","e","f","g","h","i",None, None, None,None, None,None])
        tree2 = createTreeFromList(["a","b","c","d","e","f","g","h","i",None, None, None,None, None,None])
        self.assertEqual(compareTrees(tree1, tree2), True)
        self.assertEqual(printTreefinal(tree1), printTreefinal(tree2))

        tree1 = createTreeFromList(["a"])
        tree2 = createTreeFromList(["a"])
        self.assertEqual(compareTrees(tree1, tree2), True)

        tree1 = createTreeFromList(["a","b","c","d","e","f","g","h","i",None, None, None,None, None,None])
        tree2 = createTreeFromList(["a","b","d","c","e","f","g","h","i",None, None, None,None, None,None])
        self.assertEqual(compareTrees(tree1, tree2), False)

        tree1 = createTreeFromList(["a","b","c","d","e","f","g","h","i",None, None, None,None, None,None])
        tree2 = createTreeFromList(["a","b","d","c","e","f","g","h",None, None, None,None, None,None,None])
        self.assertEqual(compareTrees(tree1, tree2), False)

        tree1 = createTreeFromList(["b","c","d","e","f","g","h","i",None, None, None,None, None,None,None])
        tree2 = createTreeFromList(["a","b","d","c","e","f","g","h","i",None, None, None,None, None,None])
        self.assertEqual(compareTrees(tree1, tree2), False)

        tree1 = createTreeFromList(["a"])
        tree2 = createTreeFromList(["b"])
        self.assertEqual(compareTrees(tree1, tree2), False)

        tree1 = createTreeFromList(["a"])
        tree2 = createTreeFromList(["b","c",None])
        self.assertEqual(compareTrees(tree1, tree2), False)


    def testCreateTreeFromList(self):
        tree1 = createTreeFromList([])
        self.assertEqual(tree1.length(), 0)
        self.assertEqual(tree1.firstitem.getSize(), 0)
        self.assertEqual(tree1.lastitem.getSize(), 0)
        self.assertEqual(tree1.getRoot().getLeft(), None)
        self.assertEqual(tree1.getRoot().getRight(), None)
        self.assertEqual(tree1.getRoot().getParent(), None)
        self.assertEqual(tree1.getRoot().getSize(), 0)
        self.assertEqual(tree1.getRoot().getHeight(), -1)

        tree1= createTreeFromList(["a"])
        self.assertEqual(tree1.length(), 1)
        self.assertEqual(tree1.firstitem.getValue(), "a")
        self.assertEqual(tree1.lastitem.getValue(), "a")
        self.assertEqual(tree1.getRoot().getLeft().getHeight(), -1)
        self.assertEqual(tree1.getRoot().getLeft().getSize(), 0)
        self.assertEqual(tree1.getRoot().getLeft().getParent(), tree1.getRoot())
        self.assertEqual(tree1.getRoot().getRight().getHeight(), -1)
        self.assertEqual(tree1.getRoot().getRight().getSize(), 0)
        self.assertEqual(tree1.getRoot().getRight().getParent(), tree1.getRoot())
        self.assertEqual(tree1.getRoot().getSize(), 1)
        self.assertEqual(tree1.getRoot().getHeight(), 0)


        tree1= createTreeFromList(["a","b","c",None,"d","e","f"])
        self.assertEqual(tree1.length(), 6)
        self.assertEqual(tree1.firstitem.getValue(), "b")
        self.assertEqual(tree1.lastitem.getValue(),"f")
        self.assertEqual(tree1.getRoot().getSize(),6)
        self.assertEqual(tree1.getRoot().getHeight(),2)
        self.assertEqual(tree1.getRoot().getParent(), None)
        self.assertEqual(tree1.firstitem.getLeft().getHeight(), -1)
        self.assertEqual(tree1.firstitem.getRight().getHeight(), 0)
        self.assertEqual(tree1.lastitem.getLeft().getHeight(), -1)
        self.assertEqual(tree1.lastitem.getRight().getHeight(), -1)

        tree1 = createTreeFromList(["a", None, "b"])
        self.assertEqual(tree1.length(), 2)
        self.assertEqual(tree1.firstitem.getValue(), "a")
        self.assertEqual(tree1.lastitem.getValue(),"b")
        self.assertEqual(tree1.getRoot().getSize(),2)
        self.assertEqual(tree1.getRoot().getHeight(),1)
        self.assertEqual(tree1.getRoot().getParent(), None)
        self.assertEqual(tree1.firstitem.getLeft().getHeight(), -1)
        self.assertEqual(tree1.firstitem.getRight().getHeight(), 0)
        self.assertEqual(tree1.lastitem.getLeft().getHeight(), -1)
        self.assertEqual(tree1.lastitem.getRight().getHeight(), -1)


        tree1 = createTreeFromList(["a","b","c","d","e", None, None, "f"])
        self.assertEqual(tree1, False)

        tree1 = createTreeFromList(["a","b","c","d","e", None, None, "f", None, None, None, None, None, None, None])
        self.assertEqual(tree1, False)



    def testisAVL(self):
        tree=AVLTreeList.AVLTreeList()
        tree.insert(0,0)
        tree.insert(1,1)
        for i in range(2,10):
            last=tree.lastitem
            tree.createNode(last.right,i)
            tree.lastitem=tree.lastitem.right
            node=tree.root
            while(node.right!=None):
                node.setHeight(node.getHeight()+1)
                node.setSize(node.getSize()+1)
                node=node.right
            self.assertEqual(False,isAVL(tree.root))
        del tree
        tree=AVLTreeList.AVLTreeList()
        tree.insert(0,9)
        tree.insert(0,8)
        for i in range(7,-1,-1):
            first=tree.firstitem
            tree.createNode(first.left,i)
            tree.firstitem=tree.firstitem.left
            node=tree.root
            while(node.left!=None):
                node.setHeight(node.getHeight()+1)
                node.setSize(node.getSize()+1)
                node=node.left
            self.assertEqual(False,isAVL(tree.root))

        

    def testInsert_Rotations(self):
        tree1=AVLTreeList.AVLTreeList()
        tree2=AVLTreeList.AVLTreeList()
        tree3=AVLTreeList.AVLTreeList()
        tree4=AVLTreeList.AVLTreeList()
        tree1.insert(0,"2")
        tree1.insert(0,"1")
        tree1.insert(0,"0")
        tree2.insert(0,"0")
        tree2.insert(1,"1")
        tree2.insert(2,"2")
        tree3.insert(0,"0")
        tree3.insert(1,"2")
        tree3.insert(1,"1")
        tree4.insert(0,"2")
        tree4.insert(0,"0")
        tree4.insert(1,"1")
        
        root1=tree1.getRoot()
        root2=tree2.getRoot()
        root3=tree3.getRoot()
        root4=tree4.getRoot()
        self.assertEqual(True, root1.getValue()==root2.getValue() and root3.getValue()==root4.getValue())
        self.assertEqual(True, root1.getValue()==root3.getValue() and root2.getValue()==root4.getValue())
        self.assertEqual(True, root1.left.getValue()==root2.left.getValue() and root3.left.getValue()==root4.left.getValue())
        self.assertEqual(True, root1.left.getValue()==root3.left.getValue() and root2.left.getValue()==root4.left.getValue())
        self.assertEqual(True, root1.right.getValue()==root2.right.getValue() and root3.right.getValue()==root4.right.getValue())
        self.assertEqual(True, root1.right.getValue()==root3.right.getValue() and root2.right.getValue()==root4.right.getValue())
        self.assertEqual(True, tree1.first()==tree2.first() and tree3.first()==tree4.first())        
        self.assertEqual(True, tree1.first()==tree3.first() and tree2.first()==tree4.first())        
        self.assertEqual(True, tree1.last()==tree2.last() and tree3.last()==tree4.last())        
        self.assertEqual(True, tree1.last()==tree3.last() and tree2.last()==tree4.last())        
        self.assertEqual(True, tree1.listToArray()==tree2.listToArray() and tree3.listToArray()==tree4.listToArray()) 
        self.assertEqual(True, tree1.listToArray()==tree3.listToArray() and tree2.listToArray()==tree4.listToArray()) 
        self.assertEqual(True, tree1.length()==tree2.length() and tree3.length()==tree4.length())         
        self.assertEqual(True, tree1.length()==tree3.length() and tree2.length()==tree4.length())         
        a=root4.left.getHeight()
        c=root3.left.getHeight()


        self.assertEqual(True, root1.getHeight()==root2.getHeight() and root3.getHeight()==root4.getHeight())  
        self.assertEqual(True, root1.getHeight()==root3.getHeight() and root2.getHeight()==root4.getHeight())  
        tree1=AVLTreeList.AVLTreeList()
        self.assertEqual(True,  tree1.insert(0,None)==0)  
        self.assertEqual(True,  tree1.insert(1,None)==1)  
        self.assertEqual(True,  tree1.insert(0,None)==0)  
        self.assertEqual(True,  tree1.insert(0,None)==2)  
        self.assertEqual(True,  tree1.insert(2,None)==0)  
        self.assertEqual(True,  tree1.insert(0,None)==3)  
        self.assertEqual(True,  tree1.insert(0,None)==2)  
        self.assertEqual(True,  tree1.listToArray()==[None for i in range(7)])  
        self.assertEqual(True,  tree1.insert(4,None)==3)  
        self.assertEqual(True,  tree1.insert(5,None)==3)  
        self.assertEqual(True, isAVL(tree1.getRoot()))  
        self.assertEqual(True,  tree1.length()==9)  
        self.assertEqual(True,  tree1.getRoot().left.getSize()==3)  
        self.assertEqual(True,  tree1.getRoot().right.getSize()==5)  
        self.assertEqual(True,  tree1.getRoot().left.getHeight()==1)  
        self.assertEqual(True,  tree1.getRoot().getHeight()==3)  
        self.assertEqual(True,  tree1.getRoot().right.getHeight()==2)
    



    def testDelete(self):
        emptytree= AVLTreeList.AVLTreeList()
        emptytree2= AVLTreeList.AVLTreeList()
        self.assertEqual(compareTrees(emptytree, emptytree2), True)
        self.assertEqual(emptytree.first()==emptytree2.first(), True)
        self.assertEqual(emptytree.last()==emptytree2.last(), True)
        self.assertEqual(printTreefinal(emptytree), printTreefinal(emptytree2))
        for i in range(10):
            emptytree.insert(i,i)
        self.assertEqual(compareTrees(emptytree, emptytree2), False)
        for i in range(9,-1,-1):
            emptytree.delete(i)
        self.assertEqual(compareTrees(emptytree, emptytree2), True)
        self.assertEqual(emptytree.first()==emptytree2.first(), True)
        self.assertEqual(emptytree.last()==emptytree2.last(), True)
        self.assertEqual(printTreefinal(emptytree), printTreefinal(emptytree2))
        tree1= AVLTreeList.AVLTreeList()
        for i in range(6,-1,-1):
            tree1.insert(0,i)
        
        tree1.delete(4)
        tree1.delete(2)
        self.assertEqual(True,tree1.length()==5)
        self.assertEqual(True,tree1.getRoot().getValue()==3)
        self.assertEqual(True,tree1.getRoot().left.getValue()==1)
        self.assertEqual(True,tree1.getRoot().right.getValue()==5)
        self.assertEqual(True,tree1.listToArray()==[0,1,3,5,6])
        tree1.delete(0)
        tree1.insert(0,0)
        tree1.delete(1)
        tree1.delete(0)
        self.assertEqual(True,tree1.getRoot().left.getValue()==3)
        self.assertEqual(True,tree1.getRoot().right.getValue()==6)
        self.assertEqual(True,tree1.getRoot().getValue()==5)
        tree1.delete(1)
        tree1.delete(0)
        self.assertEqual(True,tree1.getRoot().getValue()==6)
        tree1.delete(0)
        self.assertEqual(True,tree1.empty())
        self.assertEqual(True,tree1.length()==0)
        for j in range(2,10):    
            for i in range(1,2**j):
                tree1.insert(i-1,i)
                self.assertEqual(True,isAVL(tree1.getRoot()))
            self.assertEqual(True,isAVL(tree1.getRoot()))                
            self.assertEqual(True,tree1.getRoot().getHeight()==j-1)
            self.assertEqual(True,tree1.getRoot().left.getSize()==tree1.getRoot().right.getSize())
            tree1.insert(2**j-1,2**j)
            self.assertEqual(True,tree1.getRoot().getHeight()==j)
            for i in range((2**j)-1,((2**(j-1))-2),-1):
                tree1.delete(i)
            self.assertEqual(True,tree1.getRoot().getHeight()==j-2)
            self.assertEqual(True,isAVL(tree1.getRoot()))
            self.assertEqual(True,tree1.getRoot().left.getSize()==tree1.getRoot().right.getSize()) 
            for i in range((2**(j-1))-2,-1,-1):
                tree1.delete(i) 
            self.assertEqual(True,tree1.getRoot().getHeight()==-1)                
            self.assertEqual(True,tree1.getRoot().getValue()==None)                
            self.assertEqual(True,tree1.empty()==True) 
         #Testcase1: Delete node with successor that has children
        tree=createTreeFromList([5,2,7,1,None,None,8])
        tree.delete(2)
        self.assertEqual(tree.getRoot().getValue(),7) 
 

    

    def testrandomTrees(self):
        tree=AVLTreeList.AVLTreeList()
        L=[]
        for j in range(50):
            for i in range(2):
                tree.insert(i,i)
                L.insert(i,i)
            for i in range(30):
                r=random.randrange(0, 1+i)
                tree.insert(r,r)
                L.insert(r,r)    
                self.assertEqual(True, tree.listToArray()==L)
                self.assertEqual(True, isAVL(tree.getRoot()))
            for i in range(20):
                r=random.randrange(0,20-i)
                self.assertEqual(True, tree.retrieve(r)==L[r])
                tree.delete(r)
                del L[r]

                T=tree.listToArray()
                self.assertEqual(True, isAVL(tree.getRoot()))              
                self.assertEqual(True, tree.listToArray()==L)
                self.assertEqual(True, tree.first()==L[0])
                a= tree.last()
                b= L[len(L)-1]
                self.assertEqual(True, tree.last()==L[len(L)-1])
                self.assertEqual(True, tree.length()==len(L))
                self.assertEqual(True, tree.listToArray()==L)

    def test_all_tree_operations(self):
        tree1=AVLTreeList.AVLTreeList()
        tree2=AVLTreeList.AVLTreeList()
        L1=[]
        L2=[]
        for i in range(17):
            L1.append(i)
            tree1.insert(i,i)
        tree2.insert(0,20)
        tree2.insert(1,22)
        tree2.insert(2,24)
        tree2.insert(0,19)
        tree2.insert(0,18)
        tree2.insert(3,21)    
        tree2.insert(5,23)    
        tree2.insert(0,17)
        L2=[i for i in range(17,25)]
        self.assertEqual(True,tree1.listToArray()==L1)
        self.assertEqual(True,tree1.length()==len(L1))
        self.assertEqual(True,tree1.first()==L1[0])
        self.assertEqual(True,tree1.last()==L1[len(L1)-1])
        self.assertEqual(True,tree2.listToArray()==L2)
        self.assertEqual(True,tree1.length()==len(L1))
        self.assertEqual(True,tree2.first()==L2[0])
        self.assertEqual(True,tree2.last()==L2[len(L2)-1])
        self.assertEqual(True,isAVL(tree2.getRoot()))
        self.assertEqual(True,isAVL(tree1.getRoot()))
        tree1.concat(tree2)
        self.assertEqual(True,isAVL(tree1.getRoot()))
        L1.extend(L2)
        self.assertEqual(True,tree1.listToArray()==L1)
        for i in range(24,19,-1):
            L1.remove(i)
            a=tree1.retrieve_node(i-2)
            tree1.delete(i)
            self.assertEqual(True,isAVL(tree1.getRoot()))
        for i in range(20):
            self.assertEqual(True,tree1.retrieve(i)==L1[i])
        for i in range(20):
            self.assertEqual(True,tree1.search(i)==L1[i])
        left=L1[:10]
        right=L1[11:]
        treesplit=tree1.split(10)
        a=treesplit[0].first()
        b=treesplit[2].first()
        c=treesplit[0].last()
        d=treesplit[2].last()
        self.assertEqual(True,treesplit[0].listToArray()==left)
        self.assertEqual(True,treesplit[0].first()==left[0])
        self.assertEqual(True,treesplit[0].last()==left[len(left)-1])
        # self.assertEqual(True,isAVL(treesplit[0]))
        self.assertEqual(True,treesplit[2].listToArray()==right)
        # self.assertEqual(True,isAVL(treesplit[2]))
        self.assertEqual(True,treesplit[1]==10)
        self.assertEqual(True,treesplit[2].first()==right[0])
        a= treesplit[2].last()
        b=right[len(right)-1]
        self.assertEqual(True,treesplit[2].last()==right[len(right)-1])

        del L1,L2,tree1,tree2,a,b,c,d,i,left,right
        ####### Test Case 2, checking split first and last########
        tree = AVLTreeList.AVLTreeList()
        for i in range(5):
            tree.insert(i,i) #[0,1,2,3,4]
        splitted=tree.split(2) # [0,1],2,[3,4]
        left=splitted[0]
        right=splitted[2]
        print((splitted[1]))
        x=1
        


    def testLargeTree(self):
        #Test case 1 Large tree built from inserts
        tree= AVLTreeList.AVLTreeList()
        for i in range(2**15):
            tree.insert(i,i)
        L=[i for i in range(2**15)]
        self.assertEqual(L,tree.listToArray())
        self.assertEqual(L[0],tree.first())
        self.assertEqual(L[len(L)-1],tree.last())
        h=tree.getRoot().getHeight()
        self.assertEqual(h<15,h>17)







    def testMediumTreesOperations(self):
        tree1= AVLTreeList.AVLTreeList()
        cnt=0
        for i in range(14,-1,-1):
            cnt+=tree1.insert(0,i)
        self.assertEqual(True,tree1.getRoot().getHeight()==3)
        self.assertEqual(True,tree1.length()==15)
        self.assertEqual(True,tree1.listToArray()==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
        self.assertEqual(True,tree1.first()==0)
        self.assertEqual(True,tree1.last()==14)
        self.assertEqual(True,tree1.getRoot().getValue()==7)
        for i in range(15,2**10-1):
            tree1.insert(i,i)
        
        self.assertEqual(True,isAVL(tree1.getRoot()))    
        self.assertEqual(True,tree1.length()==2**10-1)
        self.assertEqual(True,tree1.getRoot().getHeight()==9)
        self.assertEqual(True,tree1.getRoot().left.getSize()==tree1.getRoot().right.getSize())
        tree1.insert(2**10-1,2**10-1)
        self.assertEqual(True,tree1.getRoot().getHeight()==10)
        tree1=AVLTreeList.AVLTreeList()
        for i in range(4):
            tree1.insert(0,None)
        self.assertEqual(True,isAVL(tree1.getRoot())) 
        for i in range(12):
            tree1.insert(4,None)
        self.assertEqual(True,isAVL(tree1.getRoot())) 
        self.assertEqual(True,tree1.listToArray()==[None for i in range(16)])
        for i in range(11):
            tree1.delete(2)
        self.assertEqual(True,isAVL(tree1.getRoot())) 
        for i in range(5):
            tree1.delete(0)
        self.assertEqual(True,tree1.listToArray()==[])
        self.assertEqual(True,tree1.empty())
        tree1=AVLTreeList.AVLTreeList()
        self.assertEqual(True,  tree1.insert(0,None)==0)  
        self.assertEqual(True,  tree1.insert(1,None)==1)  
        self.assertEqual(True,  tree1.insert(0,None)==0)  
        self.assertEqual(True,  tree1.insert(0,None)==2)  
        self.assertEqual(True,  tree1.insert(2,None)==0)  
        self.assertEqual(True,  tree1.insert(0,None)==3)  
        self.assertEqual(True,  tree1.insert(0,None)==2)  
        self.assertEqual(True,  tree1.listToArray()==[None for i in range(7)])  
        self.assertEqual(True,  tree1.insert(4,None)==3)  
        self.assertEqual(True,  tree1.insert(5,None)==3)  
        self.assertEqual(True, isAVL(tree1.getRoot()))  
        self.assertEqual(True,  tree1.length()==9)  
        self.assertEqual(True,  tree1.getRoot().left.getSize()==3)  
        self.assertEqual(True,  tree1.getRoot().right.getSize()==5)  
        self.assertEqual(True,  tree1.getRoot().left.getHeight()==1)  
        self.assertEqual(True,  tree1.getRoot().getHeight()==3)  
        self.assertEqual(True,  tree1.getRoot().right.getHeight()==2) 
        for i in range(9):
            tree1.delete(0)
            self.assertEqual(True, isAVL(tree1.getRoot()))
        self.assertEqual(True,tree1.empty())

    def testRetrieve(self):
        ######################
        # Case 1: Edge Cases
        ######################
        # Testcase1: [], 0 - expected: None
        tree = createTreeFromList([])
        self.assertEqual(tree.retrieve(0), None)
        # Testcase2: [], 20 - expected: None
        self.assertEqual(tree.retrieve(20), None)
        # Testcase3: [a], 0 - expected: a
        tree = createTreeFromList(["a"])
        self.assertEqual(tree.retrieve(0), "a")
        # Testcase4: [a], 1 - expected: None
        self.assertEqual(tree.retrieve(1), None)
        

        ####################################
        # Case 2: Retrive all nodes
        ####################################
        # Testcase1: [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o], {0,1,2,3,4,5,....,15}
        tree = createTreeFromList(["h","d","l","b","f","j","n","a","c","e","g","i","k","m","o"])
        self.assertEqual(tree.retrieve(0),"a")
        self.assertEqual(tree.retrieve(1),"b")
        self.assertEqual(tree.retrieve(2),"c")
        self.assertEqual(tree.retrieve(3),"d")
        self.assertEqual(tree.retrieve(4),"e")
        self.assertEqual(tree.retrieve(5),"f")
        self.assertEqual(tree.retrieve(6),"g")
        self.assertEqual(tree.retrieve(7),"h")
        self.assertEqual(tree.retrieve(8),"i")
        self.assertEqual(tree.retrieve(9),"j")
        self.assertEqual(tree.retrieve(10),"k")
        self.assertEqual(tree.retrieve(11),"l")
        self.assertEqual(tree.retrieve(12),"m")
        self.assertEqual(tree.retrieve(13),"n")
        self.assertEqual(tree.retrieve(14),"o")
        self.assertEqual(tree.retrieve(15),None)
        self.assertEqual(tree.retrieve(-1), None)
        

        ####################################
        # Case 3: Retrive splecial node
        ####################################
        # Testcase1: retrieve root
        tree = createTreeFromList(["h","e","k","c","f","j","m","b","d",None,"g","i",None,"l","n"]) # [b,c,d,e,f,g,h,i,j,k,l,m,n]
        self.assertEqual(tree.retrieve(6), "h")
        # Testcase2: retrieve leaf
        self.assertEqual(tree.retrieve(7),"i")
        # Testcase3: retrieve node with only left son
        self.assertEqual(tree.retrieve(8),"j")
        # Testcase4: retrieve node with only right son
        self.assertEqual(tree.retrieve(4),"f")
        # Tesrcase5: retrieve lastitem
        self.assertEqual(tree.retrieve(0), "b")
        # Testcase6: retrive firstitem
        self.assertEqual(tree.retrieve(12), "n")


        ####################################
        # Case 3: Large list
        ####################################
        # Testcase1: [x1]*1023 + [A] + [x2]*1023 + [B] + [x3]*1023 + [C] + [x4]*1023
        lst = ["B","A","C"]
        for i in range (10):
            lst += ["x1"]*(2**i) + ["x2"]*(2**i) + ["x3"]*(2**i) + ["x4"]*(2**i)
        tree = createTreeFromList(lst)
        self.assertEqual(tree.retrieve(0), "x1")
        self.assertEqual(tree.retrieve(500), "x1")
        self.assertEqual(tree.retrieve(1022), "x1")
        self.assertEqual(tree.retrieve(1023), "A")
        self.assertEqual(tree.retrieve(1024), "x2")
        self.assertEqual(tree.retrieve(2000),"x2")
        self.assertEqual(tree.retrieve(2046),"x2")
        self.assertEqual(tree.retrieve(2047),"B")
        self.assertEqual(tree.retrieve(2048),"x3")
        self.assertEqual(tree.retrieve(3000),"x3")
        self.assertEqual(tree.retrieve(3070),"x3")
        self.assertEqual(tree.retrieve(3071),"C")
        self.assertEqual(tree.retrieve(3072),"x4")
        self.assertEqual(tree.retrieve(4000),"x4")
        self.assertEqual(tree.retrieve(4094),"x4")
        self.assertEqual(tree.retrieve(4095), None)

	### First Tree:        
        avl2=createTreeFromList(['f','b','h','a','d', 'g','i', None, None, 'c', 'e' ,None, None, None, None])
        self.assertEqual('a', avl2.retrieve(0))
        self.assertEqual('b', avl2.retrieve(1))
        self.assertEqual('c', avl2.retrieve(2))
        self.assertEqual('d', avl2.retrieve(3))
        self.assertEqual('e', avl2.retrieve(4))
        self.assertEqual('f', avl2.retrieve(5))
        self.assertEqual('g', avl2.retrieve(6))
        self.assertEqual('h', avl2.retrieve(7))
        self.assertEqual('i', avl2.retrieve(8))
        self.assertEqual(None, avl2.retrieve(9))
        
    def testSuccessorPre(self):
        tree1= AVLTreeList.AVLTreeList()
        for i in range(14,-1,-1):
            tree1.insert(0,i)
        self.assertEqual(True, tree1.first()==0)
        self.assertEqual(True, tree1.last()==14)
        node=tree1.firstitem
        L=[]
        for i in range(15):
            L.append(node.getValue())
            node=tree1.successor(node)
        self.assertEqual(True, tree1.listToArray()==L)
        L=[]
        node=tree1.lastitem
        for i in range(15):
            L.append(node.getValue())
            node=tree1.predecessor(node)
        L.reverse()
        self.assertEqual(True, tree1.listToArray()==L)

    def testconcat(self):
        #############################
        # Case 1 - edge cases:
        #############################

        # TestCase1: [] + []  = []:
        tree1 = createTreeFromList([]) # empty list
        tree2 = createTreeFromList([]) # empty list
        heights_diff = tree1.concat(tree2)
        self.assertEqual(compareTrees(tree1, createTreeFromList([])), True)
        self.assertEqual(heights_diff, 0)

        # Testcase2: [] + [a] = [a]:
        tree1 = createTreeFromList([]) # empty list
        tree2 = createTreeFromList(["a"]) # [a]
        heights_diff = tree1.concat(tree2)
        self.assertEqual(compareTrees(tree1, createTreeFromList(["a"])), True)
        self.assertEqual(heights_diff, 1)

        # Testcase3: [a] + [] = [a]:
        tree1 = createTreeFromList(["a"]) # [a]
        tree2 = createTreeFromList([]) # empty list 
        heights_diff = tree1.concat(tree2)
        self.assertEqual(compareTrees(tree1, createTreeFromList(["a"])), True)
        self.assertEqual(heights_diff, 1)

        # Testcase4: [a,b,c] + [d,e,f] = [a,b,c,d,e,f]:
        tree1 = createTreeFromList(["b","a","c"]) # [a,b,c]
        tree2 = createTreeFromList(["e","d","f"]) # [d,e,f] 
        heights_diff = tree1.concat(tree2)
        self.assertEqual(compareTrees(tree1, createTreeFromList(["c","b","e","a",None,"d","f"])), True)
        self.assertEqual(heights_diff, 0)

        # Testcase5: [a] + [b,c,d,e,f,g,h,i,j,k,l,m,n] = [a,b,c,d,e,f,g,h,i,j,k,l,m,n]:
        tree1 = createTreeFromList(["a"]) # [a]
        tree2 = createTreeFromList(["h","e","k","c","f","j","m","b","d",None,"g","i",None,"l","n"]) # [b,c,d,e,f,g,h,i,j,k,l,m,n]
        heights_diff = tree1.concat(tree2)
        self.assertEqual(compareTrees(tree1, createTreeFromList(["h","e","k","c","f","j","m","b","d",None,"g","i",None,"l","n","a"] + [None]*15)),True)
        self.assertEqual(heights_diff,3)

        # TestCase6: [b,c,d,e,f,g,h,i,j,k,l,m,n] + [a] = [b,c,d,e,f,g,h,i,j,k,l,m,n,a]:
        tree1 = createTreeFromList(["h","e","k","c","f","j","m","b","d",None,"g","i",None,"l","n"]) # [b,c,d,e,f,g,h,i,j,k,l,m,n]
        tree2 = createTreeFromList(["a"]) # [a]
        heights_diff = tree1.concat(tree2)
        self.assertEqual(compareTrees(tree1, createTreeFromList(["h","e","k","c","f","j","m","b","d",None,"g","i",None,"l","n"]+[None]*15+["a"])),True)
        self.assertEqual(heights_diff, 3)


        # TestCase7: [b,c,d,e,f,g,h,i,j,k,l,m,n] + [] = [b,c,d,e,f,g,h,i,j,k,l,m,n]:
        tree1 = createTreeFromList(["h","e","k","c","f","j","m","b","d",None,"g","i",None,"l","n"]) # [b,c,d,e,f,g,h,i,j,k,l,m,n]
        tree2 = createTreeFromList([]) #[]
        heights_diff = tree1.concat(tree2)
        self.assertEqual(compareTrees(tree1, createTreeFromList(["h","e","k","c","f","j","m","b","d",None,"g","i",None,"l","n"])),True)
        self.assertEqual(heights_diff, 4)

        # Testcase8: [] + [b,c,d,e,f,g,h,i,j,k,l,m,n] = [b,c,d,e,f,g,h,i,j,k,l,m,n]:
        tree1 = createTreeFromList([]) #[]
        tree2 = createTreeFromList(["h","e","k","c","f","j","m","b","d",None,"g","i",None,"l","n"]) # [b,c,d,e,f,g,h,i,j,k,l,m,n]
        heights_diff = tree1.concat(tree2)
        self.assertEqual(compareTrees(tree1, createTreeFromList(["h","e","k","c","f","j","m","b","d",None,"g","i",None,"l","n"])),True)
        self.assertEqual(heights_diff, 4)

        # TestCase9: [a] + [a] = [a,a]:
        tree1 = createTreeFromList(["a"])
        tree2 = createTreeFromList(["a"])
        heights_diff = tree1.concat(tree2)
        self.assertEqual(compareTrees(tree1, createTreeFromList(["a","a",None])),True)
        self.assertEqual(heights_diff, 0)
        ######################################################################

        ###########################
        # Case 2 - Rebalance cases:
        ###########################

        # Testcase10: (one right rebalance needded) [a,b,c,x] + [A,B,C,D,E] = [a,b,c,x,A,B,C,D,E]
        tree1 = createTreeFromList(["b","a","c",None, None,None,"x"]) # [a,b,c,x]
        tree2 = createTreeFromList(["D","B","E","A","C",None, None]) # [A,B,C,D,E]
        heights_diff = tree1.concat(tree2)
        self.assertEqual(compareTrees(tree1, createTreeFromList(["x","b","D","a","c","B","E"]+[None]*4+["A","C",None, None])),True)
        self.assertEqual(heights_diff, 0)

        # Testcase11: (opposite if Testcase10) [A,B,C,D,E] + [a,b,c,x] = [A,B,C,D,E,a,b,c,x]
        # Here deleteing the lastitem will cause a rotaion
        tree1 = createTreeFromList(["D","B","E","A","C",None, None]) # [A,B,C,D,E]
        tree2 = createTreeFromList(["b","a","c",None, None,None,"x"]) # [a,b,c,x]
        heights_diff = tree1.concat(tree2)
        self.assertEqual(compareTrees(tree1, createTreeFromList(["E","B","b","A","D","a","c"]+[None]*2+["C",None, None, None,None, "x"])),True)
        self.assertEqual(heights_diff, 0)

        # TestCase12: [a,b,c,x] + [A,B,C,D,E,F,G,H] = [a,b,c,x,A,B,C,D,E,F,G,H]
        tree1 = createTreeFromList(["b","a","c",None, None,None,"x"]) # [a,b,c,x]
        tree2 = createTreeFromList(["F","D","H","B","E","G",None,"A","C"]+[None]*6) # [A,B,C,D,E,F,G,H]
        heights_diff = tree1.concat(tree2)
        self.assertEqual(compareTrees(tree1, createTreeFromList(["D","x","F","b","B","E","H","a","c","A","C",None,None,"G",None])),True)
        self.assertEqual(heights_diff,1)

        # TestCase13: (opposite of Testcase12)  [A,B,C,D,E,F,G,H] + [a,b,c,x]= [A,B,C,D,E,F,G,H,a,b,c,x]
        tree1 = createTreeFromList(["F","D","H","B","E","G",None,"A","C"]+[None]*6) # [A,B,C,D,E,F,G,H]
        tree2 = createTreeFromList(["b","a","c",None, None,None,"x"]) # [a,b,c,x]
        heights_diff = tree1.concat(tree2)
        self.assertEqual(compareTrees(tree1, createTreeFromList(["H","D","b","B","F","a","c","A","C","E","G",None,None,None,"x"])),True)
        self.assertEqual(heights_diff,1)


        # Testcase14: (one left rebalance needded) - [A,B,C,D,E] + [a,b,c] = [A,B,C,D,E,a,b,c]
        tree1 = createTreeFromList(["B","A","D",None, None, "C","E"])
        tree2 = createTreeFromList(["b","a","c"])
        heights_diff = tree1.concat(tree2)
        self.assertEqual(compareTrees(tree1, createTreeFromList(["E","B","b","A","D","a","c",None,None,"C"]+[None]*5)),True)
        self.assertEqual(heights_diff, 1)

        # Testcase15: opposite of Testcase14: 
        tree1 = createTreeFromList(["b","a","c"])
        tree2 = createTreeFromList(["B","A","D",None, None, "C","E"])
        heights_diff = tree1.concat(tree2)
        self.assertEqual(compareTrees(tree1, createTreeFromList(["B","c","D","b","A","C","E","a"]+[None]*7)),True)
        self.assertEqual(heights_diff,1)


        # TODO:
        # many rotations rebalance - is it possible?

        ###########################
        # Case 3 - Large lists
        ###########################

        # TestCase13: [a]*1023 + [x]*1023:
        tree1 = createTreeFromList(["a"]*1023) # [a]*1023
        tree2 = createTreeFromList(["x"]*1023) # [x]*1023
        heights_diff = tree1.concat(tree2)
        lst = ["a"]
        for i in range(9):
            lst += ["a"]*(2**i) + ["x"]*(2**i)
        lst += ["a"]*511 + [None] + ["x"]*512
        result = createTreeFromList(lst)
        self.assertEqual(compareTrees(tree1, createTreeFromList(lst)), True)
        self.assertEqual(heights_diff,0)

        # TODO:
        # concat a 10-leveled tree (~2047 nodes) with 20-leveled tree (~1048576 nodes)
        lst1 = ["Y","X","Z"]
        for i in range(10): #20 was too much
            lst1 += ["x1"]*(2**i) + ["x2"]*(2**i) + ["x3"]*(2**i) + ["x4"]*(2**i)
        
        lst2 = ["B","A","C"]
        for j in range(5):
            lst2 += ["a1"]*(2**j) + ["a2"]*(2**j) + ["a3"]*(2**j) + ["a4"]*(2**j)
        
        tree1 = createTreeFromList(lst1)
        tree2 = createTreeFromList(lst2)
        heights_diff = tree1.concat(tree2)
        exp_lst = lst1+lst2
        self.assertEqual(exp_lst, tree1.listToArray())
        self.assertEqual(heights_diff, 5)

        ####################################
        # Case 4 - Different Maxinum States
        ####################################

        # Testcase1: max is a leaf [a,b,c,d,e,f,g] + [x,y,z] = [a,b,c,d,e,f,g,x,y,z]
        tree1 = createTreeFromList(["d","b","f","a","c","e","g"])
        tree2 = createTreeFromList(["y","x","z"])
        heights_diff = tree1.concat(tree2)
        self.assertEqual(compareTrees(createTreeFromList(["d","b","g","a","c","f","y"]+[None]*4+["e",None,"x","z"]), tree1),True)
        self.assertEqual(heights_diff, 1)

        # max is not a leaf
        # Testcase2: [a,b,c,d] + [x,y,z] = [a,b,c,d,x,y,z]
        tree1 = createTreeFromList(["b","a","d",None, None,"c",None])
        tree2 = createTreeFromList(["y","x","z"])
        heights_diff = tree1.concat(tree2)
        self.assertEqual(compareTrees(tree1, createTreeFromList(["d","b","y","a","c","x","z"])), True)
        self.assertEqual(heights_diff, 1)

        # max deletion will cause a single rotation (right-left rotation)
        # Testcase3: [a,b,c,d,e,f,g,h] + [x,y,z] = [a,b,c,d,e,f,g,h,x,y,z]
        tree1 = createTreeFromList(["f","d","g","b","e",None,"h","a","c"]+[None]*6)
        tree2 = createTreeFromList(["y","x","z"])
        heights_diff = tree1.concat(tree2)
        new_tree = createTreeFromList(["d","b","h","a","c","f","y"] +[None]*4 + ["e","g","x","z"])
        self.assertEqual(compareTrees(tree1, new_tree), True)
        self.assertEqual(heights_diff,2)

        # max deletion will cause multiple rotations (3 rotations)
        #https://visualgo.net/en/bst?mode=AVL&create=60,9,90,5,30,80,95,3,7,20,40,70,85,92,99,2,4,8,15,25,35,50,65,75,83,93,1,10,32,48,55,62,58
        # Testcase4: [1,2,3,4,5,7,8,9,10,15,20,25,30,32,35,40,48,50,55,58,60,62,65,70,75,80,83,85,90,92,93,95,99] + [x,y,z]
        lst = ["60",\
        "9","90",\
        "5","30","80","95",\
        "3","7","20","40","70","85","92","99",\
        "2","4",None,"8","15","25","35","50","65","75","83",None,None,"93",None,None,\
        "1"] + [None]*7 + ["10"] + [None]*3 +["32",None,"48","55","62"] + [None]*15\
        +[None]*31 +["58"] + [None]*32
        tree1 = createTreeFromList(lst)
        tree2 = createTreeFromList(["y","x","z"])
        heights_diff = tree1.concat(tree2)
        new_tree_lst = ["30" ,\
            "9","60", \
            "5","20","40","80",  \
            "3","7","15","25","35","50","70","90", \
            "2", "4",None,"8","10",None,None,None, "32",None, "48","55","65","75","85","99", \
            "1"] + [None]*22 + ["58","62"] + [None]*3 +["83",None,"93","y"] \
            +[None]*60 + ["92","95","x","z"]
        new_tree = createTreeFromList(new_tree_lst)
        self.assertEqual(compareTrees(tree1, new_tree),True)
        self.assertEqual(heights_diff, 5)

        # max is the root
        # Testcase5: [a,b] + [x,y,z] = [a,b,x,y,z
        tree1 = createTreeFromList(["b","a",None])
        tree2 = createTreeFromList(["y","x","z"])
        heights_diff = tree1.concat(tree2)
        self.assertEqual(compareTrees(tree1, createTreeFromList(["y","b","z","a","x",None, None])),True)
        self.assertEqual(heights_diff,0)

        ################################################################

        tree1 = createTreeFromList(['z','x','w','y',None,None,None])
        tree2 = createTreeFromList(['a','b','c'])
        tree1.concat(tree2)
        expected = createTreeFromList(['w','x','a','y','z','b','c'])
        self.assertEqual(expected.listToArray(), tree1.listToArray())

        tree1 =createTreeFromList(['f','b','h','a','d', 'g','i', None, None, 'c', 'e' ,None, None, None, None])
        tree2 = createTreeFromList(['a','b','c'])
        tree1.concat(tree2)
        expected = createTreeFromList(['f','b','i','a','d','h','a',None, None,'c','e','g',None, 'b','c'])
        self.assertEqual(expected.listToArray(), tree1.listToArray())


    def testSplit(self):

        ########################
        # Case 1: Edge Cases:
        ########################
        # Testcase1: [a], 0 - expceted: [[],a,[]]
        tree = createTreeFromList(["a"])
        result = tree.split(0)
        self.assertEqual(compareTrees(result[0], createTreeFromList([])),True)
        self.assertEqual(result[1], "a")
        self.assertEqual(compareTrees(result[2], createTreeFromList([])),True)
        
        # Testcase2: [a,b], 0 - expected: [[], a, [b]]
        tree = createTreeFromList(["a",None,"b"])
        result = tree.split(0)
        self.assertEqual(compareTrees(result[0],createTreeFromList([])),True)
        self.assertEqual(result[1], "a")
        self.assertEqual(compareTrees(result[2], createTreeFromList(["b"])), True)

        # Another option:
        tree = createTreeFromList(["b","a",None])
        result = tree.split(0)
        self.assertEqual(compareTrees(result[0],createTreeFromList([])),True)
        self.assertEqual(result[1], "a")
        self.assertEqual(compareTrees(result[2], createTreeFromList(["b"])), True)


        # Testcase3: [a,b], 1 - expected: [[a],b,[]]
        tree = createTreeFromList(["a",None,"b"])
        result = tree.split(1)
        self.assertEqual(compareTrees(result[0],createTreeFromList(["a"])),True)
        self.assertEqual(result[1], "b")
        self.assertEqual(compareTrees(result[2], createTreeFromList([])),True)

        # Another option:
        tree = createTreeFromList(["b","a",None])
        result = tree.split(1)
        self.assertEqual(compareTrees(result[0],createTreeFromList(["a"])),True)
        self.assertEqual(result[1], "b")
        self.assertEqual(compareTrees(result[2], createTreeFromList([])),True)

        # Testcase4: [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o], 7 - expected: [[a,b,c,d,e,f,g], h, [i,j,k,l,m,n,o]]
        tree = createTreeFromList(["h","d","l","b","f","j","n","a","c","e","g","i","k","m","o"])
        result = tree.split(7)
        self.assertEqual(compareTrees(result[0], createTreeFromList(["d","b","f","a","c","e","g"])),True)
        self.assertEqual(result[1],"h")
        self.assertEqual(compareTrees(result[2], createTreeFromList(["l","j","n","i","k","m","o"])),True)

        # Testcase5: [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o], 14 - expected: [[a,b,c,d,e,f,g,h,i,j,k,l,m,n], o, []]
        tree = createTreeFromList(["h","d","l","b","f","j","n","a","c","e","g","i","k","m","o"])
        result = tree.split(14)
        self.assertEqual(compareTrees(result[0], createTreeFromList(["h","d","l","b","f","j","m","a","c","e","g","i","k",None,"n"])),True)
        self.assertEqual(result[1],"o")
        self.assertEqual(compareTrees(result[2], createTreeFromList([])),True)

        # Testcase6: [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o], 0 - expected: [[], a, [b,c,d,e,f,g,h,i,j,k,l,m,n,o]]
        tree = createTreeFromList(["h","d","l","b","f","j","n","a","c","e","g","i","k","m","o"])
        result = tree.split(0)
        self.assertEqual(compareTrees(result[0], createTreeFromList([])),True)
        self.assertEqual(result[1],"a")
        self.assertEqual(compareTrees(result[2], createTreeFromList(["h","d","l","c","f","j","n","b",None,"e","g","i","k","m","o"])),True)


        #############################
        # Case 2: Splitter Node State
        #############################
        # Testcase1: splitter is a leaf
        tree = createTreeFromList(["d","b","f","a","c","e","g"])
        result = tree.split(2)
        self.assertEqual(compareTrees(result[0], createTreeFromList(["a",None,"b"])),True)
        self.assertEqual(result[1],"c")
        self.assertEqual(compareTrees(result[2], createTreeFromList(["f","e","g","d",None,None,None])),True)

        # Testcase2: splitter is an inner node
        tree = createTreeFromList(["d","b","g","a","c","f","h"]+[None]*4+["e"]+[None]*2 +["i"])
        result = tree.split(5)
        self.assertEqual(compareTrees(result[0], createTreeFromList(["b","a","d",None,None,"c","e"])),True)
        self.assertEqual(result[1], "f")
        self.assertEqual(compareTrees(result[2], createTreeFromList(["h","g","i"])),True)

        # Testcase3: splitter is the root
        tree = createTreeFromList(["d","b","g","a","c","f","h"]+[None]*4+["e"]+[None]*2 +["i"])
        result = tree.split(3)
        self.assertEqual(compareTrees(result[0], createTreeFromList(["b","a","c"])),True)
        self.assertEqual(result[1], "d")
        self.assertEqual(compareTrees(result[2], createTreeFromList(["g","f","h","e",None,None,"i"])),True)

        # Testcase4: splitter has only left child (Tested in Testcase2)

        # Testcase5: splitter has only right child
        tree = createTreeFromList(["d","b","g","a","c","f","h"]+[None]*4+["e"]+[None]*2 +["i"])
        result = tree.split(7)
        self.assertEqual(compareTrees(result[0], createTreeFromList(["d","b","f","a","c","e","g"])),True)
        self.assertEqual(result[1], "h")
        self.assertEqual(compareTrees(result[2], createTreeFromList(["i"])),True)


        ####################################
        # Case 3: Different Joins Scenarios
        ####################################
        # Testcase1: High number of Joins  - tested in Case 6
        # Testcase2: only left Joins - tested any time the max is the splitter
        # Testcase3: only right Joins - tested any time the min is the splitter
        # Testcase4: join causes long rebalance (high number of rotations) - is it possible?


        ####################################
        # Case 4: Random
        ####################################
        # Testcase1: splitter index is randomly chosen
        for k in range (100):
            lst = ["B","A","C"]
            for i in range (10):
                lst += ["x1"]*(2**i) + ["x2"]*(2**i) + ["x3"]*(2**i) + ["x4"]*(2**i)
            tree = createTreeFromList(lst)
            tree_list = tree.listToArray()
            i = random.randint(0,tree.length()-1)
            result = tree.split(i)
            self.assertEqual(tree_list[:i], result[0].listToArray())
            self.assertEqual(tree_list[i], result[1])
            self.assertEqual(tree_list[i+1:len(tree_list)], result[2].listToArray())
            self.assertEqual(isAVL(result[0].getRoot()), True)
            self.assertEqual(isAVL(result[2].getRoot()),True)



        ####################################
        # Case 5: Chain of Splits
        ####################################
        # Testcase1: create a list and split it by half, then split each result by half and so on
        lst = ["B","A","C"]
        for i in range (10):
            lst += ["x1"]*(2**i) + ["x2"]*(2**i) + ["x3"]*(2**i) + ["x4"]*(2**i)
        tree = createTreeFromList(lst)
        while tree.length()>0:
            #printTreefinal(tree)
            tree_list = tree.listToArray()
            k = tree.length()//2
            result = tree.split(k)
            self.assertEqual(result[0].listToArray(), tree_list[:k])
            self.assertEqual(result[1], tree_list[k])
            self.assertEqual(result[2].listToArray(), tree_list[k+1:])
            self.assertEqual(isAVL(result[0].getRoot()),True)
            self.assertEqual(isAVL(result[2].getRoot()),True)
            tree = result[0]


        ####################################
        # Case 6: Large list
        ####################################
        # Testcase1: [x1]*1023 + [A] + [x2]*1023 + [B] + [x3]*1023 + [C] + [x4]*1023 split by index 1000
        lst = ["B","A","C"]
        for i in range (10):
            lst += ["x1"]*(2**i) + ["x2"]*(2**i) + ["x3"]*(2**i) + ["x4"]*(2**i)
        tree = createTreeFromList(lst)
        result = tree.split(1000)
        exp1 = ["x1"]*1000
        exp2 = ["x1"]*22 + ["A"] + ["x2"]*1023 + ["B"] + ["x3"]*1023 + ["C"] + ["x4"]*1023
        self.assertEqual(result[0].listToArray(), exp1)
        self.assertEqual(result[1], "x1")
        self.assertEqual(result[2].listToArray(), exp2)

        # Testcase2: [x1]*1023 + [A] + [x2]*1023 + [B] + [x3]*1023 + [C] + [x4]*1023 split by index 1023
        lst = ["B","A","C"]
        for i in range (10):
            lst += ["x1"]*(2**i) + ["x2"]*(2**i) + ["x3"]*(2**i) + ["x4"]*(2**i)
        tree = createTreeFromList(lst)
        result = tree.split(1023)
        exp1 = ["x1"]*1023
        exp2 = ["x2"]*1023 + ["B"] + ["x3"]*1023 + ["C"] + ["x4"]*1023
        self.assertEqual(result[0].listToArray(), exp1)
        self.assertEqual(result[1], "A")
        self.assertEqual(result[2].listToArray(), exp2)


        # Testcase3: [x1]*1023 + [A] + [x2]*1023 + [B] + [x3]*1023 + [C] + [x4]*1023 split by index 3000
        lst = ["B","A","C"]
        for i in range (10):
            lst += ["x1"]*(2**i) + ["x2"]*(2**i) + ["x3"]*(2**i) + ["x4"]*(2**i)
        tree = createTreeFromList(lst)
        result = tree.split(3000)
        exp1 = ["x1"]*1023 + ["A"] + ["x2"]*1023 + ["B"] + ["x3"]*952
        exp2 = ["x3"]*70 + ["C"] + ["x4"]*1023
        self.assertEqual(result[0].listToArray(), exp1)
        self.assertEqual(result[1], "x3")
        self.assertEqual(result[2].listToArray(), exp2)

        # Testcase4: [x1]*1023 + [A] + [x2]*1023 + [B] + [x3]*1023 + [C] + [x4]*1023 split by index 4094
        lst = ["B","A","C"]
        for i in range (10):
            lst += ["x1"]*(2**i) + ["x2"]*(2**i) + ["x3"]*(2**i) + ["x4"]*(2**i)
        tree = createTreeFromList(lst)
        result = tree.split(4094)
        exp1 = ["x1"]*1023 + ["A"] + ["x2"]*1023 + ["B"] + ["x3"]*1023 + ["C"] + ["x4"]*1022
        exp2 = []
        self.assertEqual(result[0].listToArray(), exp1)
        self.assertEqual(result[1], "x4")
        self.assertEqual(result[2].listToArray(), exp2)


        # Testcase5: [x1]*1023 + [A] + [x2]*1023 + [B] + [x3]*1023 + [C] + [x4]*1023 split by index 0
        lst = ["B","A","C"]
        for i in range (10):
            lst += ["x1"]*(2**i) + ["x2"]*(2**i) + ["x3"]*(2**i) + ["x4"]*(2**i)
        tree = createTreeFromList(lst)
        result = tree.split(0)
        exp1 = []
        exp2 = ["x1"]*1022 + ["A"] + ["x2"]*1023 + ["B"] + ["x3"]*1023 + ["C"] + ["x4"]*1023
        self.assertEqual(result[0].listToArray(), exp1)
        self.assertEqual(result[1], "x1")
        self.assertEqual(result[2].listToArray(), exp2)






        ######################
        # Case 7: General
        ######################

        tree = createTreeFromList(['a','b','c',None,'d','e','f',None,None,None,None,None,'g',None,None])
        result = tree.split(4)
        self.assertEqual(result[1], 'g')
        self.assertEqual(result[0].listToArray(), ['b','d','a','e'])
        self.assertEqual(result[2].listToArray(),['c','f'])
        left_lst=result[0]
        right_lst=result[2]


    def testSearch(self):
        ####################################
        # Case 1: Edge Cases
        ####################################

        # Testcase1: [], "" - expected: -1
        tree = createTreeFromList([])
        self.assertEqual(tree.search(""), -1)

        # Testcase2: [a], "a" - expected: 0
        tree = createTreeFromList(["a"])
        self.assertEqual(tree.search("a"), 0)

        # Testcase3: [a], "b" - expected: -1
        tree = createTreeFromList(["a"])
        self.assertEqual(tree.search("b"),-1)


        ####################################
        # Case 2: Search all nodes
        ####################################
        # Testcase4: [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o], {a,b,c,d,e,f,g,h,i,j,k,l,m,n,o} - expected: {0,1,2,3,...,14}
        tree = createTreeFromList(["h","d","l","b","f","j","n","a","c","e","g","i","k","m","o"])
        self.assertEqual(tree.search("a"),0)
        self.assertEqual(tree.search("b"),1)
        self.assertEqual(tree.search("c"),2)
        self.assertEqual(tree.search("d"),3)
        self.assertEqual(tree.search("e"),4)
        self.assertEqual(tree.search("f"),5)
        self.assertEqual(tree.search("g"),6)
        self.assertEqual(tree.search("h"),7)
        self.assertEqual(tree.search("i"),8)
        self.assertEqual(tree.search("j"),9)
        self.assertEqual(tree.search("k"),10)
        self.assertEqual(tree.search("l"),11)
        self.assertEqual(tree.search("m"),12)
        self.assertEqual(tree.search("n"),13)
        self.assertEqual(tree.search("o"),14)
        self.assertEqual(tree.search("x"),-1)



        ####################################
        # Case 3: Search special node
        ####################################
        # Testcase1: search root
        tree1 =createTreeFromList(['f','b','h','a','d','g','i', None, None, 'c', 'e' ,None, None, None, None])
        self.assertEqual(tree1.search("f"),5)
        # Testcase2: search leaf
        self.assertEqual(tree1.search("c"),2)
        # Testcase3: search inner node
        self.assertEqual(tree1.search("d"),3)
        # Testcase4: search a node with only left son
        tree1 =createTreeFromList(['f','b','h','a','d','g','i', None, None, 'c', None ,None, None, None, None])
        self.assertEqual(tree1.search("d"), 3)
        # Testcase5: search a node with only right son
        tree1 =createTreeFromList(['f','b','h','a','d','g','i', None, None, None, 'e' ,None, None, None, None])
        self.assertEqual(tree1.search("d"), 2)
        # Testcase6: search lastitem
        self.assertEqual(tree1.search("a"),0)
        # Testcase7: search firstitem
        self.assertEqual(tree1.search("i"),7)
        # Testcase8: Verify None is not in the list
        self.assertEqual(tree1.search(None),-1)




        ################################################################################
        # Case 4: Search in a large tree / search when value has multiple apearences 
        ################################################################################
        # List = [a]*63 + [x] + [b]*63 + [y] + [c]*63 + [z] + [d]*63
        # search "a" - expected: 0
        # search "b" - expected: 100
        # search "c" - expected: 200
        # search "d" - expected: 300
        # search "e" - expected: 400
        # search "d" - expected: 500
        tree = createTreeFromList(["y","x","z","a","b","c","d"]+["a"]*2+["b"]*2+["c"]*2+["d"]*2+["a"]*4+["b"]*4+["c"]*4+["d"]*4+["a"]*8+["b"]*8+["c"]*8+["d"]*8+["a"]*16+["b"]*16+["c"]*16+["d"]*16+["a"]*32+["b"]*32+["c"]*32+["d"]*32)
        self.assertEqual(tree.search("a"), 0)
        self.assertEqual(tree.search("b"),64)
        self.assertEqual(tree.search("c"),128)
        self.assertEqual(tree.search("d"),192)
        self.assertEqual(tree.search("x"), 63)
        self.assertEqual(tree.search("y"), 127)
        self.assertEqual(tree.search("z"), 191)
        # Testcase2: [a,a,a], "a" - expected: 0
        tree = createTreeFromList(["a","a","a"])
        self.assertEqual(tree.search("a"), 0)
        # Testcase3: [b,a,a], "a" - expected: 1
        tree = createTreeFromList(["a","b","a"])
        self.assertEqual(tree.search("a"),1)
        # Testcase4: [a,b,c,d,e,e,f], "e" - expected: 4
        tree = createTreeFromList(["d","b","e","a","c","e","f"])
        self.assertEqual(tree.search("e"),4)



        tree1 = createTreeFromList(['x','y','z','p','w','u','v',None, None,'q',None, None, None, None, None])
        self.assertEqual(tree1.search('p'),0)
        self.assertEqual(tree1.search('y'),1)
        self.assertEqual(tree1.search('q'),2)
        self.assertEqual(tree1.search('w'),3)
        self.assertEqual(tree1.search('x'),4)
        self.assertEqual(tree1.search('u'),5)
        self.assertEqual(tree1.search('z'),6)
        self.assertEqual(tree1.search('v'),7)
        self.assertEqual(tree1.search('a'),-1)

        tree2 = createTreeFromList(['p','w','z','p','w','z','v',None, None,'q',None, None, None, None, None])
        self.assertEqual(tree2.search('z'),5)
        self.assertEqual(tree2.search('p'),0)
        self.assertEqual(tree2.search('w'),1)




if __name__ == '__main__':
    unittest.main()



