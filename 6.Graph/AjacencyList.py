
class Vertex:
	def __init__(self, id):
		self._id = id
		self._connectedTo = {}
		
	def addNeighbor(self, nbrId, weight=0):
		self._connectedTo[nbrId] = weight
		
	def getConnections(self):
		return self.connectedTo.keys()
		
	def getId(self):
		return self._id
		
	def getWeight(self, nbrId):
		return self._connectedTo[nbrId]
		

class Graph:
	def __init__(self):
		self._vertList = {}
		self._numVertices = 0
		
	def addVertex(self, id):
		newVertex = Vertex(id)
		self._vertList[id] = newVertex
		self._numVertices += 1
		return newVertex
		
	def getVertex(self, id):
		return self._vertList[id]
		
	def __contain__(self, id):
		return id in self._vertList
		
	def addEdge(self, f, t, weight=0):
		if f not in self._vertList:
			n
		