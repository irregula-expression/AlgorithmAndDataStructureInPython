
class HashTable:
	
	def __init__(self, size):
		self._size = size
		self._slots = [None]*size
		self._data = [None]*size
		
	def hash_function(self, key, size):
		return key % size
	
	def rehash(self, old_hash, size):
		return (old_hash + 1) % size
		
	def put(self, key, data):
		hash_value = self.hash_function(key, len(self._slots))
		
		if self._slots[hash_value] == None:
			self._slots[hash_value] = key
			self._data[hash_value] = data
		
		elif self._slots[hash_value] == key:
			self._data[hash_value] = data
			
		else:
			rehash_value = self.rehash(hash_value, len(self._slots))
			
			while self._slots[rehash_value] != None and \
				self._slots[rehash_value] != key:
				rehash_value = self.rehash(rehash_value, len(self._slots))
				
			if self._slots[rehash_value] == None:
				self._slots[rehash_value] = key
				self._data[rehash_value] = data
			else:
				self._data[rehash_value] = data
				
	def get(self, key):
		hash_value = self.hash_function(key, len(self._slots))
		start_value = hash_value
		
		while self._slots[hash_value] != None:
			if self._slots[hash_value] == key:
				return self._data[hash_value]
			else:
				hash_value = self.rehash(hash_value, len(self._slots))
				if hash_value == start_value:
					return None
		
		return None
		
	def __getitem__(self, key):
		return self.get(key)
		
	def __setitem__(self, key, data):
		return self.put(key, data)
		
h = HashTable(17)
h[54]="cat"
h[26]="dog"
h[93]="lion"
h[17]="tiger"
h[77]="bird"
h[31]="cow"
h[44]="goat"
h[55]="pig"
h[20]="chicken"
print h._slots
print h._data

print h[13]
print h[17]
print h[20]
h[20] = "duck"
print h[20]
