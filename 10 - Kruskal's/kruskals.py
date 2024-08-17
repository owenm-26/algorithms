import sys
import os
from heapq import heappop, heappush

# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from treeHelpers import createTestingWeightedTrees

def kruskals(graph):
    # sort edge weights in increasing order
    PQ = []
    for u in graph:
        for v in graph[u]:
            heappush(PQ, [graph[u][v],u,v])
    MST = []
    
    nodesConnected = set()
    edges = 0
    n = len(graph)
    print(PQ)
    while edges != n-1 and PQ:
        weight, u, v = heappop(PQ)
        if u in nodesConnected and v in nodesConnected:
            continue
        else:
            MST.append((u,v))
            nodesConnected.add(u)
            nodesConnected.add(v)
            edges +=1
    
    return MST

def kruskalsChecker():
    print(binary)
    print(kruskals(binary))

if __name__ == "__main__":
    binary, unbalanced, varyingWeights = createTestingWeightedTrees()
    kruskalsChecker()