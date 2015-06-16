class Queue:
	def __init__(self):
		self._items=[]
		
	def enqueue(self, item):
		self._items.append(item)
		
	def dequeue(self):
		return self._items.pop(0)
		
	def is_empty(self):
		return self._items == []
		
	def size(self):
		return len(self._items)
		
