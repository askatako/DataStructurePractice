class Node:
	def __init__(self, val, nextnode=None):

		self.val = val
		self.next = nextnode


class LinkedList:

	def __init__(self, head=None, tail=None):
		self.head = head
		self.tail = tail
		self.size = 0


	def insert_at_end(self, linked_list, new_value):

		new_node = Node(new_value)

		if linked_list.head is None:
			linked_list.head, linked_list.tail = new_node, new_node

		else:
			new_node.head = linked_list.head
			linked_list.next, linked_list.tail = new_node, new_node
			
		linked_list.size += 1

	def insert_at_head(self, linked_list, new_value):

		new_node = Node(new_value)

		if linked_list.head is None:

			linked_list.head = new_node
		else:
			new_node.next = linked_list.head
			linked_list.head = new_node
		
		linked_list.size +=1 

	def insert_at_position(self, linked_list, new_value, position):

		assert position <= linked_list.size, "position {} is out of range".format(position)
		
		increment = 0

		new_node = Node(val)
		node =linked_list.head
		previous_node = None

		while increment <= position:
		
			if increment != position:

				increment += 1
				previous_node = node
				node = node.next

			elif increment == position:

				new_node.next=previous_node.next
				previous_node.next = new_node.next
				linked_list.size +=1













	#Remove















