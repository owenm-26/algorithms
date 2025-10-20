from heapdict import heapdict 
import math
import random

class Node:
    def __init__(self, id: int):
        self.size = 1
        self.id = id
    def __repr__(self):
        return(f"{self.id}")

class UnionFind:
    def __init__(self, n:int):
        self.reps = {}
        for i in range(1,n+1):
            node = Node(id=i)
            self.reps[node] = node

    def findPathCompression(self, u: Node) -> Node:
        """Finds topmost representative and compresses the path"""
        x = u
        while self.reps[x] != x:
            self.reps[x] = self.reps[self.reps[x]]
            x = self.reps[x]
        return x

    def unionUpdate(self, u: Node, v: Node, minHeap: heapdict, maxComp: list, minComp:list):
        """Combines two nodes components and finds the min/max component size"""
        componentU = self.findPathCompression(u)
        componentV = self.findPathCompression(v)

        if componentU != componentV:
            smaller = componentU if componentU.size < componentV.size else componentV
            larger = componentV if smaller == componentU else componentU

            # delete stale entries
            del minHeap[componentU]
            del minHeap[componentV]

            self.reps[smaller] = larger
            larger.size = larger.size + smaller.size

            # Add merged component
            minHeap[larger] = larger.size

            maxComp.append(max(maxComp[-1], larger.size))
        else:
            maxComp.append(maxComp[-1])
        
        minComp.append(minHeap.peekitem()[1])

    def addRandomEdge(self,E:set) -> tuple:
        """Adds a random connection that doesn't already exist"""
        keys = list(self.reps.keys())

        # Choose a random key from the list
        u = random.choice(keys)
        v = random.choice(keys)
        while u == v or (u,v) in E or (v,u) in E:
            u = random.choice(keys)
            v = random.choice(keys)
        
        E.add((u,v))
        return (u,v)

def componentSizes(n:int):
    """Returns a list of the smallest and largest component sizes at each timestamp"""
    limit = 1/2 * math.comb(n, 2)
    E = set()
    minComp, maxComp = [1], [1]

    UF = UnionFind(n=n)
    minHeap = heapdict({node: 1 for node in UF.reps})

    t=1
    while(t < limit and maxComp[-1] != n):
        u,v = UF.addRandomEdge(E=E)
        UF.unionUpdate(u=u, v=v, minHeap=minHeap, minComp=minComp, maxComp=maxComp)
        t+=1
    
    return maxComp, minComp

if __name__ == "__main__":
    maxComp, minComp = componentSizes(n=50)
    print(maxComp, minComp)



