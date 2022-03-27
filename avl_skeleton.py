#username - complete info
#id1      - 208772715 
#name1    - Dvir Bargai 
#id2      - 208992883
#name2    - Or Shemesh 



"""A class represnting a node in an AVL tree"""

from operator import attrgetter
from platform import node
from tkinter import N
from tkinter.messagebox import NO
from turtle import left
import math


class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 

	@type value: str
	@param value: data of your node
	@inv index in list = $left.size+1
	@$height=-1 implies this is a virtual node
	"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		self.size = 0
		
	def setFields(self, value, left, right, parent, height, size):
		self.value = value
		self.left = left
		self.right = right
		self.parent = parent
		self.height = height
		self.size = size
	 


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

	"""" returns the size

	@rtype: int
	@returns: the size of self
	"""
	def getSize(self):
		return self.size
	
	
	""" returns the Balance Factor
		@rtype: int
		@returns: the Balance Factor of self
		@pre: self represent a "Real Node"
	"""	
	def getBF(self):
		return self.getLeft().getHeight() - self.getRight().getHeight()



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

	"""returns whether self is a leaf

	@rtype: bool
	@returns: True if self is a leaf node, False otherwise.
	"""
	def isLeaf(self):
		if self.left.isRealNode() or self.right.isRealNode():
			return False
		return True

	
	"""returns whether self is has one real child

	@rtype: bool
	@returns: True if self has one real child, False otherwise.
	"""
	def isMediumNode(self):
		cnt=0
		if self.left.isRealNode():
			cnt+=1
		if self.right.isRealNode():
			cnt+=1
		if cnt==1: 
			return True
		return False

	"""returns the medium node's real child 
	@pre: node.isMediumNode()==True
	@rtype: AVLNode
	@returns: The node of the real child of self.
	"""
	def realChild(self):
		if self.left.isRealNode():
			return self.left
		else:
			return self.right
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
	@returns: the value of the i'th item in the list
	"""
	def retrieve(self, i):
		return self.retrieve_node(i).value

	"""retrieves the i'th node in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: AVLNode
	@returns: the node of the i'th item in the list
	"""
	def retrieve_node(self, i):
		node=self.getRoot()
		while i!=node.left.size: #loop expects virtual node to exist and have size=0
			if node.left.size >i:
				node=node.left
			else:
				i = i-node.left.size-1
				node=node.right
		return node



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

	"""deletes a node and turn him to "virtual Node"

	@type Node: AVLNode
	@pre: Node is a leaf 
	@rtype: None
	@returns: None
	"""
	def deleteNode(self,node):
		node.setValue(None)
		node.setLeft(None)
		node.setRight(None)
		node.setHeight(-1)
		node.setSize(0)
		return None

	def deleteMiddleNode(self,node):
		parent=node.getParent()
		if parent.left==node: #node is a left son	
			parent.setLeft(node.realChild())
			parent.left.setParent(parent)
		else: #node is a right son
			parent.setRight(node.realChild())
			node.right.setParent(parent)
		return None

	"""inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	# def insert(self, i, val):
	# 	if i==self.length(): #maintain first and last pointers
	# 		self.lastitem=val
	# 	if i==0:
	# 		self.firstitem=val
	# 	rebalance=0
	# 	if self.empty(): 
	# 		self.createRoot(val)
	# 	else:
	# 		rebalance= self.insertRec(i,val,self.root,rebalance)
		
	# 	return rebalance 

	"""inserts val using recursion

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we insert
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self,i,val):
		if self.empty(): 
			self.createRoot(val)
			self.firstitem=val
			self.lastitem=val
			return 0
		if i==0:
			self.firstitem=val
		if i==self.length(): #maintain first and last pointers
			self.lastitem=val
			max=self.retrieve_node(i-1)
			node=max.getRight()
			self.createNode(node,val)
		else:
			curr=self.retrieve_node(i)
			if not curr.getLeft().isRealNode():
				node=curr.getLeft()
				self.createNode(node,val)
			else:
				parent=self.predecessor(curr)
				node=parent.getRight()
				self.createNode(node,val)
		return self.rebalance(node)




	def insertRec(self, i, val,node,rebalance): #recursion 
		if not node.isRealNode():
			self.createNode(node,val)
		
		elif i<=node.left.size:
			node.size+=1
			rebalance+=self.insertRec(i, val ,node.left,rebalance)
		else: 

			node.size+=1
			rebalance+=self.insertRec(i-1-(node.left.size), val ,node.right,rebalance)
		
		node.setHeight(1+max(node.left.height,node.right.height)) #set new height if needed
		BF=node.getBF()
		if abs(BF)>=2:
			
			if (BF)>1: #BF=+2
				if node.left.getBF()==1: #BF of left son is +1
					self.rotateRight(node,node.left)
					return 1
				else: #BF of the left son is -1
					self.rotateLeftThenRight(node,node.left,node.left.right) #left then right
					return 2
			else: #BF=-2
				if node.right.getBF()==-1: #BF of right son is -1
					self.rotateLeft(node,node.right)
					return 1
				else: #BF of the right son is +1
					self.rotateRightThenLeft(node,node.right,node.right.left) #right then left
					return 2
		
		return rebalance

	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		cnt_rotations=0
		if self.length()!=1:
			if i==self.length()-1:
				self.lastitem=self.retrieve(i-1)
			if i==0:
				self.firstitem=self.retrieve(1)
		else: #delete the only item and its the root
			self.lastitem=None
			self.firstitem=None
		node= self.retrieve_node(i)
		if node.isLeaf():
			self.deleteNode(node)
			if self.getRoot()!=node:
				parent=node.getParent()
			else:
				parent=node
		elif node.isMediumNode(): #node has one real child
			if self.getRoot()==node:
				self.root=node.realChild()
				self.root.setParent(None)
			else:
				self.deleteMiddleNode(node)
			parent=node.getParent()
		else: #node has two real children
			successor=self.retrieve_node(i+1) #physical deleted node
			parent=successor.getParent() 
			node.setValue(successor.getValue())
			self.deleteNode(successor) if successor.isLeaf() else self.deleteMiddleNode(successor)
		if parent==None: 
			return 0
		if parent.getValue()!=None:
			parent.setSize(parent.left.getSize()+parent.right.getSize()+1)
			parent.setHeight(1+max(parent.left.getHeight(),parent.right.getHeight()))
			cnt_rotations=self.rebalance(parent)
		return cnt_rotations



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
		node = None
		middle = self.last
		self.delete(self.length-1)
		if self.length > lst.length:
			node=self.findMaximalNodeByHeight(lst.height)
		else:
			node=self.findMinimalNodeByHeight(self.height)
			self.concat_redirect(middle, lst.getRoot(),node)
		
		
		return None

	"""rebalancing the tree from a given node to the root
	@rtype: int
	@returns: a counter of the number of rotations performed
	"""

	def rebalance(self, start_node):
		cnt=0
		while (start_node !=None):
			if abs(start_node.getBF())==2: 
				if start_node.getBF()<0:
					if start_node.getRight().getBF()==1:
						start_node=self.rotateRightThenLeft(start_node, start_node.getRight(), start_node.getRight().getLeft())
						cnt+=2
					else:
						#if self.getright().getBF() not in [0,-1]:
						#	print("Impossible BF")
						start_node=self.rotateLeft(start_node, start_node.getRight())
						cnt+=1
				else: #BF is +2
					#if start_node.getBF()!=2:
					#	print("Impossible BF")
					if start_node.getLeft().getBF()==-1:
						start_node=self.rotateLeftThenRight(start_node, start_node.getLeft(), start_node.getLeft().getRight())
						cnt+=2
					else:
						#if self.getright().getBF() not in [0,1]:
						#	print("Impossible BF")
						start_node=self.rotateRight(start_node, start_node.getLeft())
						cnt+=1
			else:
				prev_height=start_node.getHeight()
				self.updateHeight(start_node)
				if prev_height!=start_node.getHeight(): cnt+=1 
			self.updateSize(start_node)
			start_node=start_node.getParent()
		return cnt
	
	"""returns minimal-index node with height<=h
	@rtype: AVLNodes
	@pre: 0 ≤ h ≤ self.root.height
	@type h: int
	"""
	def findMinimalNodeByHeight(self, h):
		node = self.root
		while node.height>h:
			node=node.left
		return node


	"""returns maximal-index node with height<=h
	@rtype: AVLNodes
	@pre: 0 ≤ h ≤ self.root.height
	@type h: int
	"""
	def findMaximalNodeByHeight(self, h):
		node = self.root
		while node.height>h:
			node=node.right
		return node
	
	def concat_redirect(self, mid, newRoot, minNode):
		mid.setLeft(self.getRoot)
		mid.setRight(minNode)
		self.getRoot().setParent(minNode.getParent())
		mid.setParent(minNode.getParent())
		minNode.setParent(mid)
		self.root = newRoot


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
	@rtype: AVLNode
	@returns: The parent of the given nodes
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
		self.updateSize(parent,leftSon)
		self.updateHeight(parent,leftSon)
		return leftSon
	
	"""right rotation to balance the list

	@type parent: AVLNode
	@pre: parent.left.height-parent.right.height==-2
	@param parent: the old parent which we need to rotate for balancing
	@type leftSon: AVLNode
	@pre: leftSon.left.height-leftSon.right.height==1
	@param parent: the old left son which we need to rotate for balancing
	@rtype: AVLNode
	@returns: The parent of the given nodes
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
		self.updateSize(parent,rightSon)
		self.updateHeight(parent,rightSon)
		return rightSon

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
	@returns: The parent of the given nodes
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
		self.updateSize(parent,leftSon,leftRightSon)
		self.updateHeight(parent,leftSon,leftRightSon)
		return leftRightSon

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
	@returns: The parent of the given nodes
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
		self.updateSize(parent,rightSon,rightLeftSon)
		self.updateHeight(parent,rightSon,rightLeftSon)
		return rightLeftSon

	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		return self.root

	"""calculates and sets the size of all given nodes by order

	@rtype: None
	@returns: the root, None if the list is empty
	"""

	def updateSize(self,node1,node2=None,node3=None):
		node1.setSize(1+node1.left.size+node1.right.size)
		if node2!=None:
			node2.setSize(1+node2.left.size+node2.right.size)
		if node3!=None:
			node3.setSize(1+node3.left.size+node3.right.size)

	"""calculates and sets the height of all given nodes by order

	@rtype: None
	@returns: the root, None if the list is empty
	"""
	def updateHeight(self,node1,node2=None,node3=None):
		node1.setHeight((1+max(node1.left.getHeight(),node1.right.getHeight())))
		if node2!=None:
			node2.setHeight((1+max(node2.left.getHeight(),node2.right.getHeight())))
		if node3!=None:
			node3.setHeight((1+max(node3.left.getHeight(),node3.right.getHeight())))

	"""finds predecessor of a given node
	@pre: self.isRealNode(node.getLeft()) 
	@type: AVLNode
	@rtype: AVLNode
	@returns: the predecessor
	"""
	def predecessor(self,node):
		start=node.getLeft()
		while (start.getRight().isRealNode()):
			start=start.getRight()
		return start			

def main():
	pass
	mytree= AVLTreeList()
	
	

#main()