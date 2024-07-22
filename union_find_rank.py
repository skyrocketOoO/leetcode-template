class UnionFindWithRank:
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
    def union(self, x, y, ranker):
        rootX = self.find(x)
        rootY = self.find(y)
        # Set the root with lower rank as the parent
        isLess = ranker.less(rootX, rootY)
        if isLess:
            self.parents[rootX] = rootY
        else:
            self.parents[rootY] = rootX
    
class RankDirectlyCompare:
    def less(self, x, y):
        return x < y
    
class RankGroupSize:
    def __init__(self):
        self.sizes = {}
    
    def less(self, x, y):
        if x not in self.sizes:
            self.sizes[x] = 1
        if y not in self.sizes:
            self.sizes[y] = 1
        if self.sizes[x] <= self.sizes[y]:
            self.sizes[y] += 1
            return True
        self.sizes[x] += 1
        return False


if __name__ == "__main__":
    # Example usage:
    elements = [1, 2, 3, 4, 5]
    uf = UnionFindWithRank(elements)
    uf.union(1, 2)
    uf.union(2, 3)

    # Find the root of an element
    print(uf.find(1))  # Output: 3 (since 1, 2, and 3 are in the same group)
    print(uf.find(4))  # Output: 4 (since 4 is in its own group)
