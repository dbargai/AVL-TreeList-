import unittest
import avl_skeleton as AVLTreeList
import math


"""This method is for testing ONLY and returns a legal tree created from a given list
@pre: list of strings which satisfies the following format:
	list length is a power of 2 and
	index 0 is the root,
	next 2 indexes are the sons of the root,
	next 4 indexes are the sons of the root's sons
	and so on by this pattern while a "missing son" will be represented by None
@post: False if list represents illegal tree, compatible AVLTreeList otherwise
@rtype: AVLTreeList
"""

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


def createTreeFromList(lst):
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
		##Create leaf node:
		node = AVLTreeList.AVLNode(None)
		node.setFields(lst[i], AVLTreeList.AVLNode(None), AVLTreeList.AVLNode(None), None, 0, 1)
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


class TestMavnatProject1(unittest.TestCase):
    
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
        self.assertEqual(True,cnt==11)
        self.assertEqual(True,tree1.getRoot().getValue()==7)
        for i in range(15,2**10-1):
            tree1.insert(i,i)
        self.assertEqual(True,tree1.length()==2**10-1)
        a=tree1.getRoot().getHeight()
        self.assertEqual(True,tree1.getRoot().getHeight()==9)
        self.assertEqual(True,tree1.getRoot().left.getSize()==tree1.getRoot().right.getSize())
        tree1.insert(2**10-1,2**10-1)
        self.assertEqual(True,tree1.getRoot().getHeight()==10)
        

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
        

    def testConcat(self):
        tree1 = createTreeFromList(['z','x','w','y',None,None,None])
        tree2 = createTreeFromList(['a','b','c'])
        result = tree1.concat(tree2)
        expceted = createTreeFromList(['w','x','a','y','z','b','c'])


if __name__ == '__main__':
    unittest.main()




