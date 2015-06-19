
class Node:
	
	def __init__(self, init_data):
		self._data = init_data
		self._next = None
		
	def get_data(self):
		return self._data
		
	def get_next(self):
		return self._next
		
	def set_data(self, new_data):
		self._data = new_data
		
	def set_next(self, next_node):
		self._next = next_node	

		
class UnorderedList:
	
	def __init__(self):
		self._head = None
		
	def is_empty(self):
		return self._head == None
		
	def add(self, a_data):
		new_node = Node(a_data)
		new_node.set_next(self._head)
		self._head = new_node
		
	def size(self):
		current_node = self._head
		count = 0
		while current_node != None:
			count += 1
			current_node = current_node.get_next()
			
		return count
		
	def search(self, the_data):
		current_node = self._head
		while current_node != None:
			if current_node.get_data() == the_data:
				return True
			else:
				current_node = current_node.get_next()
		
		return False
		
	def remove(self, the_data):
		current_node = self._head
		previous_node = None
		found = False
		while not found:
			if current_node.get_data() == the_data:
				found = True
			else:
				previous_node = current_node
				current_node = current_node.get_next()
		
		if previous_node == None:
			self._head = current_node.get_next()
		else:
			previous_node.set_next(current_node.get_next())
			
			