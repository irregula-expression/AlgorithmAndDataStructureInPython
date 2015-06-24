
class Vertex:
	def __init__(self, id):
		self._id = id
		self._connectedTo = {}
		
	def addNeighbor(self, nbrVertex, weight=0):
		self._connectedTo[nbrVertex] = weight
		
	def getConnections(self):
		return self._connectedTo.keys()
		
	def getId(self):
		return self._id
		
	def getWeight(self, nbrVertex):
		return self._connectedTo[nbrVertex]
		

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
		
	def addEdge(self, fromId, toId, weight=0):
		if fromId not in self._vertList:
			nv = self.addVertex(fromId)
		if toId not in self._vertList:
			nv = self.addVertex(toId)
		self._vertList[fromId].addNeighbor(self._vertList[toId], weight)
	
	def getVertices(Self):
		return self._vertList.keys()
		
	def __iter__(self):
		for vertex in self._vertList.values():
			yield vertex

	
# g = Graph()
# for i in range(6):
	# g.addVertex(i)
	
#print g._vertList

# g.addEdge(0,1,5)
# g.addEdge(0,5,2)
# g.addEdge(1,2,4)
# g.addEdge(2,3,9)
# g.addEdge(3,4,7)
# g.addEdge(3,5,3)
# g.addEdge(4,0,1)
# g.addEdge(5,4,8)
# g.addEdge(5,2,1)
	
# for v in g:
	# for w in v.getConnections():
		# print "(%s, %s)" %(v.getId(), w.getId())


