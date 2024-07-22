class UnionFind:
    def __init__(self):
        self.parents = {}  # Initialize a dictionary to store parents

    # Given an element, find the root of the group to which this element belongs.
    def find(self, x):
        # This may be the first time we see x, so set itself as the root.
        if x not in self.parents:
            self.parents[x] = x
        # If x != parents[x], we use the find function again on x's parent parents[x]
        # until we find the root and set it as the parent (value) of x in parents.
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    # Given two elements x and y, merge the groups to which they belong.
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        # Set the root of y(rootY) as the root of the root of x(rootX)
        self.parents[rootX] = rootY

    def groups(self, eles):
        groups = 0
        for ele in eles:
            if self.find(ele) == ele:
                groups += 1
        return groups

if __name__ == "__main__":
    # Example usage:
    uf = UnionFind()
    uf.union(1, 2)
    uf.union(2, 3)

    # Find the root of an element
    print(uf.find(1))  # Output: 3 (since 1, 2, and 3 are in the same group)
    print(uf.find(4))  # Output: 4 (since 4 is in its own group)
