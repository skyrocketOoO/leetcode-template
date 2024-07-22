from collections import defaultdict

class Graph:
	def __init__(self, vertices):
		self.graph = defaultdict(list)
		self.V = vertices
		self.in_deg = [0] * vertices

	def addEdge(self, u, v):
		self.graph[u].append(v)
		self.in_deg[v] += 1

	# if the vertex is in cyclic, it will not add into res
	def topologicalSort(self):
		q = []
		for i in range(self.V):
			if self.in_deg[i] == 0:
				q.append(i)
        
		res = []
		while q:
			i = q.pop(0)
			res.append(i)
			for j in self.graph[i]:
				self.in_deg[j] -= 1
				if self.in_deg[j] == 0:
					q.append(j)
	
		return res

# Driver Code
if __name__ == '__main__':
	g = Graph(6)
	g.addEdge(5, 2)
	g.addEdge(5, 0)
	g.addEdge(4, 0)
	g.addEdge(4, 1)
	g.addEdge(2, 3)
	g.addEdge(3, 1)
	#g.addEdge(1, 3)
 
	print("Following is a Topological Sort of the given graph")

	print(g.topologicalSort())

