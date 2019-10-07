

class Node:

#Initializes a node that is used in linked list

	def __init__(self, val, nextnode=None):

		self.val = val
		self.next = nextnode

class LinkedList:

#Makes a singly linked list

	def __init__(self, head=None, tail=None):
		self.head = head
		self.tail = tail
		self.size = 0


	def get_size(self):

		"""
		Returns the size of the linked list
		"""
		return self.size

	def get_head(self):

		"""
		Returns the head node of the linked list
		"""

		return self.head

	def get_tail(self):

		"""
		Returns the tail node of the linked list
		"""

		return self.tail


	def insert(self, new_value):

		"""
		Inserts the node at the end of the linked list
		"""

		new_node = Node(new_value)

		if self.head is None:
			self.head, self.tail = new_node, new_node

		else:
			self.tail.next, self.tail = new_node, new_node

		self.size += 1

	def insert_at_head(self, new_value):

		"""
		Inserts the node at the head of the linked list
		"""

		new_node = Node(new_value)

		if self.head is None:

			self.head = new_node
		else:
			new_node.next = self.head
			self.head = new_node
		
		self.size +=1 

	def insert_at_position(self, new_value, position):

		"""
		Inserts the node at a given position in the linked list
		"""

		assert position <= self.size, "position {} is out of range".format(position)
		
		increment = 0

		new_node = Node(new_value)
		node =self.head
		previous_node = None

		while increment <= position:
			print(increment)

			if increment != position:

				previous_node = node

				if node.next is not None:
					node = node.next

				elif node.next is None and position == increment:
					continue

			elif increment == position:
				print("here")
				new_node.next=node
				previous_node.next = new_node
				self.size +=1

			increment += 1



	def remove_at_position(self, position):

		"""
		Removes the node at the stated position
		"""

		assert position <= self.size, "position {} is out of range".format(position)
		
		increment = 0

		node =self.head
		previous_node = None

		while increment <= position:
		
			increment += 1

			if increment != position:

				previous_node = node

				if node.next is not None:
					node = node.next

				elif node.next is None and position == increment:
					continue

			elif increment == position:

				previous_node.next = node.next
				self.size -=1











