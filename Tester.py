import unittest
from venv import create
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
                       

    def testrandomTrees(self):
        random.seed(10)
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
        right=L1[10:]
        treesplit=tree1.split(10)
        a=treesplit[0].listToArray()
        # self.assertEqual(True,treesplit[0].listToArray()==left)
        # self.assertEqual(True,treesplit[0].first()==left[0])
        # self.assertEqual(True,treesplit[0].last()==left[len(left)-1])
        # self.assertEqual(True,isAVL(treesplit[0]))
        # self.assertEqual(True,treesplit[2].listToArray()==right)
        # self.assertEqual(True,isAVL(treesplit[2]))
        # self.assertEqual(True,treesplit[1].listToArray()==[10])
        # self.assertEqual(True,treesplit[2].first()==right[0])
        # self.assertEqual(True,treesplit[2].last()==right[len(right)-1])



        


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

    def testConcat(self):
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
        tree = createTreeFromList(['a','b','c',None,'d','e','f',None,None,None,None,None,'g',None,None])
        result = tree.split(4)
        self.assertEqual(result[1], 'g')
        self.assertEqual(result[0].listToArray(), ['b','d','a','e'])
        self.assertEqual(result[2].listToArray(),['c','f'])
        left_lst=result[0]
        right_lst=result[2]


    def testSearch(self):
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



