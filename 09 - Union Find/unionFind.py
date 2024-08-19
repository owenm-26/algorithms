class DisjointSet:
    def __init__(self, graph) -> None:
        self.parents = {}
        self.ranks = {}
        for u in graph:
            self.parents[u] = u
            self.ranks[u] = 0
        

    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, nodeA, nodeB):
        groupA = self.find(nodeA)
        groupB = self.find(nodeB)

        if groupA != groupB:
            if self.ranks[groupA] < self.ranks[groupB]:
                self.parents[groupA] = groupB
            elif self.ranks[groupA] > self.ranks[groupB]:
                self.parents[groupB] = groupA
            else:
                self.parents[groupB] = groupA
                self.ranks[groupA] += 1

    def __repr__(self) -> str:
        return f"DisjointSet(parents={self.parents}, ranks={self.ranks})"

def unionFindChecker():
    ds = DisjointSet(4)
    assert ds.parents == [0, 1, 2, 3]
    ds.union(0, 1)
    assert ds.parents == [0, 0, 2, 3]
    ds.union(2, 3)
    assert ds.parents == [0, 0, 2, 2]
    ds.union(1, 2)
    assert ds.parents == [0, 0, 0, 2]
    print('Union Find tests passed!')

if __name__ == "__main__":
    unionFindChecker()
