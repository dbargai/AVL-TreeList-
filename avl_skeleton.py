#username - dvirbargai
#id1      - 208772715 
#name1    - Dvir Bargai 
#id2      - 208992883
#name2    - Or Shemesh 

 
"""
	@invs:
	1. Node x is consodered virtual node iff (x.left=None and x.right=None and x.size=0 and x.height=-1)
	2. Node x is a leaf iff (x.left is virtual and x.right is virtual)
	3. There is no node with only one son as None
"""
class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 

	@type value: str
	@param value: data of your node
	@$height=-1 @implies this is a virtual node
	@Time Complexity: O(1)
	"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		self.size = 0


	##################################
	# Geters:
	##################################
	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	@Time Complexity: O(1)
	"""
	def getLeft(self):
		return self.left

	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	@Time Complexity: O(1)
	"""
	def getRight(self):
		return self.right

	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	@Time Complexity: O(1)
	"""
	def getParent(self):
		return self.parent

	"""return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	@Time Complexity: O(1)
	"""
	def getValue(self):
		return self.value

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	@Time Complexity: O(1)
	"""
	def getHeight(self):
		return self.height

	"""" returns the size

	@rtype: int
	@returns: the size of self
	@Time Complexity: O(1)
	"""
	def getSize(self):
		return self.size
	
	""" returns the Balance Factor
		@rtype: int
		@returns: the Balance Factor of self
		@pre: self represent a "Real Node"
		@Time Complexity: O(1)
	"""	
	def getBF(self):
		return self.getLeft().getHeight() - self.getRight().getHeight()

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	@Time Complexity: O(1)
	"""	
	def isRealNode(self):
		return self.getLeft()!=None or self.getRight()!=None


	##################################
	# Seters:
	##################################
	"""sets left child

	@type node: AVLNode
	@param node: a node
	@Time Complexity: O(1)
	"""
	def setLeft(self, node):
		self.left=node
		return None

	"""sets right child

	@type node: AVLNode
	@param node: a node
	@Time Complexity: O(1)
	"""
	def setRight(self, node):
		self.right=node
		return None

	"""sets parent

	@type node: AVLNode
	@param node: a node
	@Time Complexity: O(1)
	"""
	def setParent(self, node):
		self.parent=node
		return None

	"""sets value

	@type value: str
	@param value: data
	@Time Complexity: O(1)
	"""
	def setValue(self, value):
		self.value=value
		return None

	"""sets the balance factor of the node

	@type h: int
	@param h: the height
	@Time Complexity: O(1)
	"""
	def setHeight(self, h):
		self.height=h
		return None
	
	"""sets the size of the node

	@type size: int
	@param size: the size of the sub-tree 
	@Time Complexity: O(1)
	"""
	def setSize(self, size):
		self.size=size
		return None


	##############################
	# Additional:
	##############################
	"""returns whether self is a leaf

	@rtype: bool
	@returns: True if self is a leaf node, False otherwise.
	@Time Complexity: O(1)
	"""
	def isLeaf(self):
		if self.getLeft().isRealNode() or self.getRight().isRealNode():
			return False
		return True
	
	"""returns whether self is has exactly one real son
	@rtype: bool
	@returns: True if self has exactly one real child, False otherwise.
	@Time Complexity: O(1)
	"""
	def isMediumNode(self):
		cnt=0
		if self.getLeft().isRealNode():
			cnt+=1
		if self.getRight().isRealNode():
			cnt+=1
		if cnt==1: 
			return True
		return False

	"""returns the medium node's real child 
	@pre: node.isMediumNode()==True
	@rtype: AVLNode
	@returns: The node of the real child of self.
	@Time Complexity: O(1)
	"""
	def realChild(self):
		if self.getLeft().isRealNode():
			return self.getLeft()
		else:
			return self.getRight()

	"""returns true if self is a left son and False if not
	@Time Complexity: O(1)
	"""
	def isLeftSon(self):
		return self.getParent()!=None and self.getParent().getLeft() is self


"""
A class implementing the ADT list, using an AVL tree.
@invs: 
	1. T is AVLTreeList implies T has at least one child (may be virtual)
	2. For any ACLTreeList T: T.root.size = number of elements in the represented list
	3. AVLTreeList T is empty iff T.root is virtual
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  
	@Time Complexity: O(1)
	"""
	def __init__(self):
		self.root = AVLNode(None)
		self.firstitem= self.root
		self.lastitem= self.root
		# add your fields here

	################################
	# Geters:
	################################
	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, virtual if the list is empty
	@Time Complexity: O(1)
	"""
	def getRoot(self):
		return self.root

	"""returns the firstitem of the tree representing the list

	@rtype: AVLNode
	@returns: first item of the list
	@Time Complexity: O(1)
	"""
	def getFirstItem(self):
		return self.firstitem

	"""returns the lastitem of the tree representing the list

	@rtype: AVLNode
	@returns: last item of the list
	@Time Complexity: O(1)
	"""
	def getLastItem(self):
		return self.lastitem
	

	################################
	# Seters:
	################################
	"""sets the root of the tree

	@type r: AVLNode
	@param r: the root node of the tree
	@Time Complexity: O(1)
	"""
	def setRoot(self, r):
		self.root = r

	"""sets the firstitem of the tree

	@type first: AVLNode
	@param first: the first item of the list
	@Time Complexity: O(1)
	"""
	def setFirstItem(self, first):
		self.firstitem = first

	"""sets the lastitem of the tree

	@type last: AVLNode
	@param last: the last item of the list
	@Time Complexity: O(1)
	"""

	def setLastItem(self, last):
		self.lastitem = last

	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	@Time Complexity: O(1)
	"""
	def empty(self):
		return True if self.length()==0 else False




	"""retrieves the value of the i'th item in the list
	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the value of the i'th item in the list
	@Time compexity: O(logn)
	"""
	def retrieve(self, i):
		if (i<0 or i>self.length()-1):
			return None
		else:
			return self.retrieve_node(i).getValue()

	"""retrieves the i'th node in the list
	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: AVLNode
	@returns: the node of the i'th item in the list
	@Time Complexity: O(logn)
	"""
	def retrieve_node(self, i):
		node=self.getRoot()
		while i!=node.getLeft().getSize(): #loop expects virtual node to exist and have size=0
			if node.getLeft().getSize()>i:
				node=node.getLeft()
			else:
				i = i-node.getLeft().getSize()-1
				node=node.getRight()
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
		node.getLeft().setParent(node)
		node.setRight(AVLNode(None))
		node.getRight().setParent(node)
		node.setHeight(0)
		node.setSize(node.getSize()+1)
		return None


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
	
	"""deletes a middle node and "skip" over him

	@type Node: AVLNode
	@pre: Node has one child
	@rtype: None
	@returns: None
	"""

	def deleteMiddleNode(self,node):
		parent=node.getParent()
		if parent.getLeft()==node: #node is a left son	
			parent.setLeft(node.realChild())
			parent.getLeft().setParent(parent)
		else: #node is a right son
			parent.setRight(node.realChild())
			node.getRight().setParent(parent)
		return None

	"""inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	@Time Complexity: O(logn)
	"""

	def insert(self,i,val):
		if self.empty(): 
			self.createNode(self.root,val) 
			self.setFirstItem(self.root)
			self.setLastItem(self.root)
			return 0
		if i==self.length(): #maintain first and last pointers
			max=self.getLastItem()
			node=max.getRight()
			self.createNode(node,val)
			self.setLastItem(node)
		else:
			curr=self.retrieve_node(i) 
			if not curr.getLeft().isRealNode(): 
				node=curr.getLeft()
				self.createNode(node,val)
			else:
				parent=self.predecessor(curr)
				node=parent.getRight()
				self.createNode(node,val)
			if i==0:
				self.setFirstItem(node)
		return self.rebalance(node)

	
	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	@Time Complexity: O(logn)
	"""
	def delete(self, i):
		cnt_rotations=0
		first=False
		last=False
		if self.length()!=1:  #check if deleted node is first and/or last
			last=True if i==self.length()-1 else False
			first=True if i==0 else False
		node= self.retrieve_node(i)
		if last:
			self.setLastItem(self.predecessor(node))
		if first:
			self.setFirstItem(self.successor(node))
		if node.isLeaf():
			self.deleteNode(node)
			if self.getRoot()!=node:
				parent=node.getParent()
			else:
				return 0
		elif node.isMediumNode(): #node has one real child
			if self.getRoot()==node:
				self.setRoot(node.realChild())
				self.getRoot().setParent(None)
			else:
				self.deleteMiddleNode(node)
			parent=node.getParent()
		else: #node has two real children
			successor=self.successor(node) #physical deleted node
			parent=successor.getParent() 
			node.setValue(successor.getValue())
			self.deleteNode(successor) if successor.isLeaf() else self.deleteMiddleNode(successor)
		cnt_rotations=self.rebalance(parent)
		return cnt_rotations


	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	@Time Complexity: O(1)
	"""
	def first(self):
		return self.firstitem.getValue()

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	@Time Complexity: O(1)
	"""
	def last(self):
		return self.lastitem.getValue()

	"""returns an array representing list

	@rtype: list
	@returns: a list of strings representing the data structure
	@Time Complexity: O(n)
	"""
	def listToArray(self): #Use inorder recursion to append each node to the array
		array = []
		def listToArrayRec(node,array):
			if node.getSize() == 0:
				return None
			listToArrayRec(node.getLeft(),array)
			array.append(node.getValue())
			listToArrayRec(node.getRight(),array)
			return None
		
		listToArrayRec(self.getRoot(),array)
		return array

	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	@Time Complexity: O(1)
	"""
	def length(self):
		return self.getRoot().getSize()

	"""join left_lst and right_lst using a 'middle' node.
	@type left_lst, right_lst: AVLTreeList
	@type mid = AVLNode
	@post: left_lst = left_lst + mid + right_lst
	@returns: root of left_lst after the join operation
	@Time Complexity: O(|self.height - right_lst.height|)
	"""
	def join (self, mid, right_lst):
		# set lastitem, firstitem:
		if self.length() == 0:
			self.setFirstItem(mid) if mid!=None else right_lst.getFirstItem()
		if right_lst.length() == 0:
			self.setLastItem(mid) if mid!=None else self.getLastItem()
		else:
			self.setLastItem(right_lst.getLastItem())
		
		# link between relevant nodes based on trees' heights:
		if self.getRoot().getHeight() > right_lst.getRoot().getHeight():
			node=self.findMaximalNodeByHeight(right_lst.getRoot().getHeight())
			self.link_nodes(mid, node, right_lst.getRoot(), node.getParent(), 'R')
		elif self.getRoot().getHeight() < right_lst.getRoot().getHeight():
			node=right_lst.findMinimalNodeByHeight(self.getRoot().getHeight())
			self.link_nodes(mid, self.getRoot(), node, node.getParent(), 'L')
			self.setRoot(right_lst.getRoot())
		else:
			node=right_lst.getRoot()
			self.link_nodes(mid, self.getRoot(), node, None, None)
			self.setRoot(mid)
		
		# execute rebalance starting from mid.parent:
		self.rebalance(mid.getParent())


	"""returns a tree which its root is the given node
	@rtype: AVLTreeList
	@pre: node is AVLNode
	@post: $node is the root of $tree
	@post: $node.parent=None. Note that this means $node is "disconnected" from its old tree
	@Time Complexity: O(1)
	"""
	@staticmethod
	def createTreeByRoot(node):
		node.setParent(None)
		tree = AVLTreeList()
		tree.root = node
		return tree

	"""splits the list at the i'th index, Time Complexity: O(logn)

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list according to whom we split
	@rtype: list
	@returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
	right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
	@ Time Complexity: O(logn)
	"""
	def split(self, i):
		# Create 2 instances of AVLTreeList which will be the lists after the split
		left_tree = AVLTreeList()
		right_tree = AVLTreeList()

		# Find splitter node
		splitter = self.retrieve_node(i)
		
		next_parent = splitter.getParent() # keep original parent 
										   # in case pointers will change during join

		# Set roots:
		left_tree.setRoot(splitter.getLeft())
		right_tree.setRoot(splitter.getRight())

		isLeft = splitter.isLeftSon()

		while next_parent != None:
			next_parent_to_set = next_parent.getParent() # keep next parent now in case 
														 # pointers will change during join
			if isLeft:
				isLeft = next_parent.isLeftSon() # update this before the join operation
												 # join in case pointers will change during join
				# create tree from parent's right son:
				tmp_right = AVLTreeList.createTreeByRoot(next_parent.getRight())
				# join trees:
				right_tree.join(next_parent, tmp_right)
			else:
				isLeft = next_parent.isLeftSon() # update this before the join operation
												 # join in case pointers will change during join
				# create trees from parent's left son:
				tmp_left = AVLTreeList.createTreeByRoot(next_parent.getLeft())
				# join trees:
				tmp_left.join(next_parent, left_tree)
				# in this case update left_tree:
				left_tree = tmp_left
			next_parent = next_parent_to_set

		# set roots parents to None:	
		left_tree.getRoot().setParent(None)
		right_tree.getRoot().setParent(None)

		# set lastitems, firstitems, add O(logn) - does not ruin complexity
		left_tree.setFirstItem(self.getFirstItem()) if i!=0 else left_tree.findMinimalNodeByHeight(0)
		left_tree.setLastItem(left_tree.findMaximalNodeByHeight(0))
		right_tree.setFirstItem(right_tree.findMinimalNodeByHeight(0))
		right_tree.lastitem = self.lastitem if left_tree.length()!=i else right_tree.findMaximalNodeByHeight(0)
		return [left_tree, splitter.getValue() ,right_tree]


	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	@Time Complexity: O(logn)
	"""
	def concat(self, lst):			
		heights_diff = abs(self.getRoot().getHeight() - lst.getRoot().getHeight())

		# edge cases: one if the lists is empty:
		if self.length()==0:
			self.root = lst.getRoot()
			self.setFirstItem(lst.getFirstItem())
			self.setLastItem(lst.getLastItem())
			return heights_diff
		if lst.length()==0:
			return heights_diff

		# if both lists aren't empty:
		val = self.lastitem.getValue()
		linker = AVLNode(val)
		self.delete(self.length()-1)
		self.join(linker, lst)
		return heights_diff

	"""rebalancing the tree from a given node to the root
	@rtype: int
	@returns: a counter of the number of rotations performed
	@Time Complexity: O(logn)
	"""
	def rebalance(self, start):
		cnt=0
		while (start !=None):
			if abs(start.getBF())==2:
				if start.getBF()<0:
					if start.getRight().getBF()==1:
						start=self.rotateRightThenLeft(start, start.getRight(), start.getRight().getLeft())
						cnt+=2
					else:
						start=self.rotateLeft(start, start.getRight())
						cnt+=1
				else: #BF is +2
					if start.getLeft().getBF()==-1:
						start=self.rotateLeftThenRight(start, start.getLeft(), start.getLeft().getRight())
						cnt+=2
					else:
						start=self.rotateRight(start, start.getLeft())
						cnt+=1
			else:
				prev_height=start.getHeight()
				self.updateHeight(start)
				if prev_height!=start.getHeight(): cnt+=1 
			self.updateSize(start)
			start=start.getParent()
		return cnt
	

	"""returns minimal-index node with height<=h
	@rtype: AVLNodes
	@pre: 0 ≤ h ≤ self.root.height
	@type h: int
	@Time Complexity: O(self.height - h)
	"""
	def findMinimalNodeByHeight(self, h):
		node = self.getRoot()
		while node.getHeight()>h:
			node = node.getLeft()
		return node

	"""returns maximal-index node with height<=h
	@rtype: AVLNodes
	@pre: 0 ≤ h ≤ self.root.height
	@type h: int
	@Time Complexity: O(self.height - h)
	"""
	def findMaximalNodeByHeight(self,h):
		node = self.getRoot()
		while node.height>h:
			node = node.getRight()
		return node

	"""set sons and parents fields for join
	@rtype: None
	@pre: $side == 'R' or $side = 'L'
	@post: $mid's sons are $left and $right and its parent is $parent
	@Time Complexity: O(1)
	"""
	@staticmethod
	def link_nodes(mid, left, right, parent, side):
		mid.setLeft(left)
		mid.getLeft().setParent(mid)
		mid.setRight(right)
		mid.getRight().setParent(mid)
		mid.setParent(parent)
		mid.setSize(mid.getLeft().getSize()+mid.getRight().getSize()+1)
		mid.setHeight(max(mid.getLeft().getHeight(), mid.getRight().getHeight())+1)
		if parent!=None:
			if (side=='R'):
				parent.setRight(mid)
			else:
				parent.setLeft(mid)


	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	@Time Complexity: O(n)
	"""
	def search(self, val):
		return self.search_rec(self.getRoot(), val, 0)

	def search_rec(self, node, val, cnt):
		if (not node.isRealNode()):
			return -1
		left=self.search_rec(node.getLeft(),val, cnt)
		if left>=0:
			return left
		if node.getValue()==val:
			return cnt + node.getLeft().getSize()
		else:
			return self.search_rec(node.getRight(),val, cnt+ node.getLeft().getSize()+1)

	"""right rotation to balance the list

	@type parent: AVLNode
	@pre: parent.left.height-parent.right.height==2
	@param parent: the old parent which we need to rotate for balancing
	@type leftSon: AVLNode
	@pre: leftSon.left.height-leftSon.right.height==1
	@param parent: the old left son which we need to rotate for balancing
	@rtype: AVLNode
	@returns: The parent of the given nodes
	@Time complexity: O(1)
	"""
	def rotateRight(self,parent,leftSon): 	
		parent.setLeft(leftSon.right)
		parent.getLeft().setParent(parent)
		leftSon.setRight(parent)
		if parent==self.getRoot(): #AVL "criminal" is the tree's root
			self.setRoot(leftSon)
			leftSon.setParent(None)
		elif parent.getParent().getLeft()==parent: #parent is a left son
			parent.getParent().setLeft(leftSon)
			leftSon.setParent(parent.getParent())
		else: #parent is a right son
			parent.getParent().setRight(leftSon)
			leftSon.setParent(parent.getParent())
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
	@Time Complexity: O(1)
	"""
	def rotateLeft(self,parent,rightSon): 
		parent.setRight(rightSon.left)
		parent.getRight().setParent(parent)
		rightSon.setLeft(parent)
		if self.getRoot()==parent:
			self.setRoot(rightSon)
			rightSon.setParent(None)
		elif parent.getParent().getLeft()==parent: #parent is a left son
			parent.getParent().setLeft(rightSon)
			rightSon.setParent(parent.parent)
		else: #parent is a right son
			parent.getParent().setRight(rightSon)
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
	@Time Complexity: O(1)
	"""
	def rotateLeftThenRight(self,parent,leftSon,leftRightSon):
		parent.setLeft(leftRightSon.getRight())
		parent.getLeft().setParent(parent)
		leftSon.setRight(leftRightSon.left)
		leftSon.getRight().setParent(leftSon)
		leftRightSon.setLeft(leftSon)
		leftSon.setParent(leftRightSon)
		leftRightSon.setRight(parent)
		if self.getRoot()==parent: #if parent is root
			self.setRoot(leftRightSon)
			leftRightSon.setParent(None)		
		elif parent.getParent().getLeft()==parent: #if parent is left son
			parent.getParent().setLeft(leftRightSon)
			leftRightSon.setParent(parent.getParent())
		else:
			parent.getParent().setRight(leftRightSon)
			leftRightSon.setParent(parent.getParent())
		parent.setParent(leftRightSon)
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
	@Time Complexity: O(1)
	"""
	def rotateRightThenLeft(self,parent,rightSon,rightLeftSon):
		parent.setRight(rightLeftSon.getLeft())
		parent.getRight().setParent(parent)
		rightSon.setLeft(rightLeftSon.getRight())
		rightSon.getLeft().setParent(rightSon)
		rightLeftSon.setRight(rightSon)
		rightSon.setParent(rightLeftSon)
		rightLeftSon.setLeft(parent)
		if self.getRoot()==parent: #if parent is root
			self.setRoot(rightLeftSon)
			rightLeftSon.setParent(None)		
		elif parent.getParent().getLeft()==parent: #if parent is left son
			parent.getParent().setLeft(rightLeftSon)
			rightLeftSon.setParent(parent.getParent())
		else:
			parent.getParent().setRight(rightLeftSon)
			rightLeftSon.setParent(parent.getParent())
		parent.setParent(rightLeftSon)
		self.updateSize(parent,rightSon,rightLeftSon)
		self.updateHeight(parent,rightSon,rightLeftSon)
		return rightLeftSon

	"""calculates and sets the size of all given nodes by order

	@rtype: None
	@returns: the root, None if the list is empty
	@Time Complexity: O(1)
	"""
	def updateSize(self,node1,node2=None,node3=None):
		node1.setSize(1+node1.getLeft().getSize()+node1.getRight().getSize())
		if node2!=None:
			node2.setSize(1+node2.getLeft().getSize()+node2.getRight().getSize())
		if node3!=None:
			node3.setSize(1+node3.getLeft().getSize()+node3.getRight().getSize())

	"""calculates and sets the height of all given nodes by order

	@rtype: None
	@returns: the root, None if the list is empty
	@Time Complexity: O(1)
	"""
	def updateHeight(self,node1,node2=None,node3=None):
		node1.setHeight((1+max(node1.getLeft().getHeight(),node1.getRight().getHeight())))
		if node2!=None:
			node2.setHeight((1+max(node2.getLeft().getHeight(),node2.getRight().getHeight())))
		if node3!=None:
			node3.setHeight((1+max(node3.getLeft().getHeight(),node3.getRight().getHeight())))

	"""finds predecessor of a given node
	@pre: self.isRealNode(node.getLeft()) 
	@type: AVLNode
	@rtype: AVLNode
	@returns: the predecessor
	@Time Complexity: O(logn)
	"""
	def predecessor(self,node):
		if node.getLeft().isRealNode():
			start=node.getLeft()
			while (start.getRight().isRealNode()):
				start=start.getRight()
			return start			
		parent=node.getParent()
		while parent!=None and parent.getLeft()==node:
			node=parent
			parent=node.getParent()
		return parent
	
	"""finds successor of a given node
	Time Complexity (worst case): O(logn) - going downward only or upward only
	@pre: self.isRealNode(node.getR())
	@type: AVLNode
	@rtype: AVLNode
	@returns: the predecessor
	@Time Complexity: O(logn)
	"""
	def successor(self,node):
		if node.getRight().isRealNode():
			start=node.getRight()
			while (start.getLeft().isRealNode()):
				start=start.getLeft()
			return start			
		parent=node.getParent()
		while parent!=None and parent.getRight()==node:
			node=parent
			parent=node.getParent()
		return parent