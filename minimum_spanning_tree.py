class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        self.parent[root_x] = root_y

def kruskals_mst(graph):
    num_vertices = len(graph)
    edges = []

    # Create a list of edges (weight, u, v) from the graph
    for u in range(num_vertices):
        for v, weight in enumerate(graph[u]):
            if weight is not None:
                edges.append((weight, u, v))

    # Sort the edges by weight
    edges.sort()

    mst = []
    uf = UnionFind(num_vertices)

    for weight, u, v in edges:
        if uf.find(u) != uf.find(v):
            mst.append((u, v, weight))
            uf.union(u, v)

    return mst

if __name__ == "__main__":
    graph = [
        [None, 2, None, None, 3],
        [2, None, 4, None, 1],
        [None, 4, None, 5, 3],
        [None, None, 5, None, None],
        [3, 1, 3, None, None]
    ]

    mst = kruskals_mst(graph)
    for u, v, weight in mst:
        print(f"Edge: {u} - {v}, Weight: {weight}")