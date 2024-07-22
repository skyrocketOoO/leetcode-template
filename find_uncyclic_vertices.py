from collections import defaultdict
from typing import List

# dfs method
def find_uncyclic_vertices(graph: List[List[int]]) -> List[int]:
    # using dfs
    def dfs(u, status):
        # init to unsafe
        status[u] = 2

        for v in graph[u]:
            if status[v] == 0: # not visited
                if dfs(v, status):
                    return True
            elif status[v] == 2: # if u has edge to unsafe v, u also unsafe
                return True
        
        # if all check passed, u is safe
        status[u] = 1
        return False

    n = len(graph)
    # 0: not visited, 1: status, 2: unsafe
    status = [0] * n 
    for u in range(n):
        if status[u] == 0:
            dfs(u, status)
            
    return [u for u in range(n) if status[u] == 1]

# use topological sort, add the converse edges to the graph
def find_uncyclic_vertices_topo(graph: List[List[int]]) -> List[int]:
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

    n = len(graph)
    g = Graph(n)
    for v in range(n):
        for u in graph[v]:
            g.addEdge(u, v)
    return sorted(g.topologicalSort())


# Driver code
if __name__ == '__main__':
    graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    # answer = [2,4,5,6], sort by increment
    
    print(find_uncyclic_vertices(graph))

    print(find_uncyclic_vertices_topo(graph))

# Thanks to Divyanshu Mehta for contributing this code
