
class BinaryHeap:
	
	def __init__(self):
		self._heapList = [0]
		self._size = 0
		
    def percUp(self, idx):
		while idx/2 > 0:
			if self._heapList[idx/2] > self._heapList[idx]:
				temp = self._heapList[idx]
				self._heapList[idx] = self._heapList[idx/2]
				self._heapList[idx/2] = temp
			idx  /= 2
		
	def insert(self, key):
		self._heapList.append(key)
		self._size += 1
		self.percUp(self._size)
				
	
	def percDown(self, idx):
		while idx*2 <= self._size:
			mcIdx = self.minChildIdx(idx)
			if self._heapList[idx] > self._heapList[mcIdx]:
				temp = self._heapList[idx]
				self._heapList[idx] = self._heapList[mcIdx]
				self._heapList[mcIdx] = temp	
			idx = mcIdx
			
	def minChildIdx(self, idx):
		if idx*2+1 > self._size():
			return idx*2
		else:
			if self._heapList[idx*2] < self._heapList[idx*2+1]:
				return idx*2
			else:
				return idx*2+1
				
	def delMin(self):
		min = self._heapList[1]
		self._heapList[1] = self._heapList[self._size]
		self._size -= 1
		self._heapList.pop()
		self.percDow(1)
		return min
		
	def buildHeap(self, a_list):
		self._size = len(a_list)
		self._heapList = [0] + a_list[:]
		idx = len(a_list) / 2
		while idx > 0:
			self.percDown(idx)
			idx -= 1
			