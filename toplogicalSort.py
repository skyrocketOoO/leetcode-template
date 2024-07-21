from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list) 

    def add_edge(self, u, v):
        self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v] = []

    def topological_sort(self):
        in_degree = {u: 0 for u in self.graph}
        for u in self.graph:
            for v in self.graph[u]:
                if v not in in_degree:
                    in_degree[v] = 0
                in_degree[v] += 1

        queue = deque([u for u in self.graph if in_degree[u] == 0])
        top_order = []

        while queue:
            u = queue.popleft()
            top_order.append(u)

            for v in self.graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        if len(top_order) == len(self.graph):
            return top_order
        else:
            return "Graph has a cycle"

if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'C')
    g.add_edge('B', 'C')
    g.add_edge('D', 'C')
    g.add_edge('C', 'E')
    g.add_edge('D', 'E')
    g.add_edge('E', 'F')
    
    result = g.topological_sort()
    print("Topological Sort of the given graph:")
    print(result)
