#username - complete info
#id1      - 208772715 
#name1    - Dvir Bargai 
#id2      - 208992883
#name2    - Or Shemesh 



"""A class represnting a node in an AVL tree"""

from platform import node
from turtle import left


class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 

	@type value: str
	@param value: data of your node

	@$height=-1 implies this is a virtual node
	"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		self.size = 0
		

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""
	def getLeft(self):
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""
	def getRight(self):
		return self.right

	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def getParent(self):
		return self.parent

	"""return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""
	def getValue(self):
		return self.value

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def getHeight(self):
		a=self.height
		return self.height

	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def setLeft(self, node):
		self.left=node
		return None

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
		self.right=node
		return None

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def setParent(self, node):
		self.parent=node
		return None

	"""sets value

	@type value: str
	@param value: data
	"""
	def setValue(self, value):
		self.value=value
		return None

	"""sets the balance factor of the node

	@type h: int
	@param h: the height
	"""
	def setHeight(self, h):
		self.height=h
		return None
	"""sets the size of the node

	@type size: int
	@param size: the size of the sub-tree 
	"""
	def setSize(self, size):
		self.size=size
		return None
	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self):
		return self.left!=None or self.right!=None

	"""computes the balance factor of a given node 

	@rtype: int
	@returns: height of left son minus height of right son
	"""
	def computeBF(self):
		a=self.left.getHeight()-self.right.getHeight()
		return self.left.getHeight()-self.right.getHeight()
	# def orTester():
	# 	lst tests = [AVLNode("3"), AVLNode(""), AVLNode("733")]
	# 	tests[0].height = 10
	# 	pass

	# def testGet


"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = AVLNode(None)
		self.firstitem= None
		self.lastitem= None
		# add your fields here


	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self):
		if self.length()==0:
			return True
		return False


	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""
	def retrieve(self, i):
		return None

	"""creates a node in a specific index with two virtual leaves

	@type node: AVLNode
	@pre: 
	@param node: the "virtual" node from which we create the new real node
	@type val: any object
	@pre: 
	@param val: the value of the new node we create  
	@rtype: None
	@returns: None
	"""
	def createNode(self,node,val):
		node.setValue(val)
		node.setLeft(AVLNode(None))
		node.left.setParent(node)
		node.setRight(AVLNode(None))
		node.right.setParent(node)
		node.setHeight(0)
		node.size+=1
		return None

	
	"""creates a root when the tree is empty

	@type val: any object
	@pre: 
	@param val: the value of the new node we create  
	@rtype: None
	@returns: None
	"""
	def createRoot(self,val):
			self.root.setValue(val)
			self.root.setHeight(0)
			self.root.setSize(1)
			self.root.setLeft(AVLNode(None))
			self.root.left.setParent(self.root)
			self.root.setRight(AVLNode(None))
			self.root.right.setParent(self.root)
			self.firstitem=val
			self.lastitem=val

	
	"""inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, i, val):
		
		if i==self.length(): #maintain first and last pointers
			self.lastitem=val
		if i==0:
			self.firstitem=val
		flagRebalance=False
		if self.empty(): 
			self.createRoot(val)
		else:
			flagRebalance= self.insertRec(i,val,self.root,flagRebalance)
		
		return 1 if flagRebalance else 0

	"""inserts val using recursion

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we insert
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

	def insertRec(self, i, val,node,flag): #recursion 
		if not node.isRealNode():
			self.createNode(node,val)
		
		elif i<=node.left.size:
			node.size+=1
			flag=self.insertRec(i, val ,node.left,flag)
		else: 

			node.size+=1
			flag=self.insertRec(i-1-(node.left.size), val ,node.right,flag)
		
		node.setHeight(1+max(node.left.height,node.right.height)) #set new height if needed
		BF=node.computeBF()
		if abs(BF)>=2:
			
			if (BF)>1: #BF=+2
				if node.left.computeBF()==1: #BF of left son is +1
					self.rotateRight(node,node.left)
				else: #BF of the left son is -1
					self.rotateLeftThenRight(node,node.left,node.left.right) #left then right
			
			else: #BF=-2
				if node.right.computeBF()==-1: #BF of right son is -1
					self.rotateLeft(node,node.right)
				else: #BF of the right son is +1
					self.rotateRightThenLeft(node,node.right,node.right.left) #right then left

			flag=True #a rotation took place
		
		node.setHeight(1+max(node.left.height,node.right.height)) #set new height if needed
		return flag

	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		return -1


	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		return self.firstitem

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		return self.lastitem

	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self): #Use inorder recursion to append each node to the array
		array = []
		def listToArrayRec(Node,array):
			if Node.size == 0:
				return None
			listToArrayRec(Node.left,array)
			array.append(Node.value)
			listToArrayRec(Node.right,array)
			return None
		
		listToArrayRec(self.root,array)
		return array

	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):
		return self.root.size
		
	"""splits the list at the i'th index

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list according to whom we split
	@rtype: list
	@returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
	right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
	"""
	def split(self, i):
		return None

	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def concat(self, lst):
		return None

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):
		return None

	"""right rotation to balance the list

	@type parent: AVLNode
	@pre: parent.left.height-parent.right.height==2
	@param parent: the old parent which we need to rotate for balancing
	@type leftSon: AVLNode
	@pre: leftSon.left.height-leftSon.right.height==1
	@param parent: the old left son which we need to rotate for balancing
	@rtype: None
	@returns: None
	"""

	def rotateRight(self,parent,leftSon): 	
		parent.left=leftSon.right
		parent.left.setParent(parent)
		leftSon.right=parent
		if parent==self.root: #AVL "criminal" is the tree's root
			self.root=leftSon
			leftSon.setParent(None)
		elif parent.parent.left==parent: #parent is a left son
			parent.parent.left=leftSon
			leftSon.setParent(parent.parent)
		else: #parent is a right son
			parent.parent.right=leftSon
			leftSon.setParent(parent.parent)
		parent.setParent(leftSon)
		parent.setSize(1+parent.left.size+parent.right.size)
		leftSon.setSize(1+leftSon.left.size+leftSon.right.size)
		return None
	
	"""right rotation to balance the list

	@type parent: AVLNode
	@pre: parent.left.height-parent.right.height==-2
	@param parent: the old parent which we need to rotate for balancing
	@type leftSon: AVLNode
	@pre: leftSon.left.height-leftSon.right.height==1
	@param parent: the old left son which we need to rotate for balancing
	@rtype: None
	@returns: None
	"""

	def rotateLeft(self,parent,rightSon): 
		parent.right=rightSon.left
		parent.right.setParent(parent)
		rightSon.left=parent
		if self.root==parent:
			self.root=rightSon
			rightSon.setParent(None)
		elif parent.parent.left==parent: #parent is a left son
			parent.parent.left=rightSon
			rightSon.setParent(parent.parent)
		else: #parent is a right son
			parent.parent.right=rightSon
			rightSon.setParent(parent.parent)
		parent.setParent(rightSon)
		parent.setSize(1+parent.left.size+parent.right.size)
		rightSon.setSize(1+rightSon.left.size+rightSon.right.size)
		return None

	"""left then right rotation to balance the list

	@type parent: AVLNode
	@pre: parent.left.height-parent.right.height==2
	@param parent: the old parent which we need to rotate for balancing
	@type leftSon: AVLNode
	@pre: leftSon.left.height-leftSon.right.height==-1
	@param parent: the old left son which we need to rotate for balancing
	@type leftSon: AVLNode
	@pre: leftRightSon.left.height-leftRightSon.right.height==1
	@param parent: the right son of the left son which we need to rotate for balancing
	@rtype: AVLNode
	@returns: None
	"""

	def rotateLeftThenRight(self,parent,leftSon,leftRightSon):
		parent.left=leftRightSon.right
		parent.left.setParent(parent)
		leftSon.right=leftRightSon.left
		leftSon.right.setParent(leftSon)
		leftRightSon.left=leftSon
		leftSon.setParent(leftRightSon)
		leftRightSon.right=parent
		if self.root==parent: #if parent is root
			self.root=leftRightSon
			leftRightSon.setParent(None)		
		elif parent.parent.left==parent: #if parent is left son
			parent.parent.left=leftRightSon
			leftRightSon.setParent(parent.parent)
		else:
			parent.parent.right=leftRightSon
			leftRightSon.setParent(parent.parent)
		parent.setParent(leftRightSon)
		parent.setSize(1+parent.left.size+parent.right.size)
		leftSon.setSize(1+leftSon.left.size+leftSon.right.size)
		leftRightSon.setSize(1+leftRightSon.left.size+leftRightSon.right.size)
		return None

	"""right then left rotation to balance the list

	@type parent: AVLNode
	@pre: parent.left.height-parent.right.height==-2
	@param parent: the old parent which we need to rotate for balancing
	@type rightSon: AVLNode
	@pre: rightSon.left.height-rightSon.right.height==1
	@param parent: the old left son which we need to rotate for balancing
	@type rightSon: AVLNode
	@pre: rightLeftSon.left.height-rightLeftSon.right.height==-1
	@param parent: the left son of the right son which we need to rotate for balancing
	@rtype: AVLNode
	@returns: None
	"""

	def rotateRightThenLeft(self,parent,rightSon,rightLeftSon):
		parent.right=rightLeftSon.left
		parent.right.setParent(parent)
		rightSon.left=rightLeftSon.right
		rightSon.left.setParent(rightSon)
		rightLeftSon.right=rightSon
		rightSon.setParent(rightLeftSon)
		rightLeftSon.left=parent
		if self.root==parent: #if parent is root
			self.root=rightLeftSon
			rightLeftSon.setParent(None)		
		elif parent.parent.left==parent: #if parent is left son
			parent.parent.left=rightLeftSon
			rightLeftSon.setParent(parent.parent)
		else:
			parent.parent.right=rightLeftSon
			rightLeftSon.setParent(parent.parent)
		parent.setParent(rightLeftSon)
		parent.setSize(1+parent.left.size+parent.right.size)
		rightSon.setSize(1+rightSon.left.size+rightSon.right.size)
		rightLeftSon.setSize(1+rightLeftSon.left.size+rightLeftSon.right.size)

	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		return self.root


def main():
	mytree= AVLTreeList()
	print(mytree.insert(0,10))
	print(mytree.insert(0,9))
	print(mytree.insert(0,8))
	print(mytree.insert(0,7))
	print(mytree.insert(0,6))
	print(mytree.insert(0,5))
	print(mytree.insert(0,4))
	print(mytree.insert(0,3))
	print(mytree.insert(0,2))
	print(mytree.insert(9,11))
	print("length is " ,mytree.length())
	print("root size is",mytree.root.size)
	print("left root size",mytree.root.left.size)
	print("right root size",mytree.root.right.size)
	print("root height",mytree.root.height)
	print("root" ,mytree.root.value)
	print(mytree.listToArray())
	print(mytree.insert(10,12))
	# print(mytree.insert(11,11))
	# print(mytree.insert(12,12))
	# print(mytree.insert(0,100))
	# print(mytree.insert(14,14))
	# print(mytree.root.right.left.value)
	# print(mytree.root.right.right.value)
	print(mytree.listToArray())
	print(mytree.last())
	print(mytree.first())
	# print(mytree.listToArray())
	# ##ok
	# print(mytree.listToArray())
	# print(mytree.root.value)
	# mytree.insert(1,13)
	# print(mytree.listToArray())
	# print(mytree.listToArray())
	# mytree.insert(6,30)
	# print(mytree.listToArray())
	# print(mytree.length())
	# print(mytree.root.left.size)
	# print(mytree.root.right.size)	
	

main()
