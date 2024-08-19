import sys
import os
from heapq import heappop, heappush

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
union_find_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../09 - Union Find'))
sys.path.append(parent_dir)
sys.path.append(union_find_dir)

from treeHelpers import createTestingKruskalsTrees
from unionFind import DisjointSet

def kruskals(graph):
    # sort edge weights in increasing order
    PQ = []
    for u in graph:
        for v in graph[u]:
            heappush(PQ, [graph[u][v],u,v])
    MST = []
    n = len(graph)
    djs = DisjointSet(graph)

    while len(MST) != n-1 and PQ:
        weight, u, v = heappop(PQ)
        if djs.find(u) == djs.find(v):
            continue
        else:
            MST.append((u,v))
            djs.union(u,v)
    
    return MST

def kruskalsChecker():
    assert kruskals(simple_tree) == [('A', 'B'), ('B', 'D'), ('A', 'C')]
    assert kruskals(complete_graph) == [('A', 'B'), ('C', 'D'), ('B', 'C')]
    assert kruskals(disconnected_graph) == [('A', 'B'), ('B', 'C'), ('D', 'E')]
    assert kruskals(varying_weights_graph) == [('D', 'F'), ('A', 'B'), ('A', 'D'), ('B', 'E'), ('C', 'F')]
    assert kruskals(sparse_graph) == [('D', 'E'), ('A', 'B'), ('B', 'C')]
    assert kruskals(cyclic_graph) == [('A', 'B'), ('B', 'D'), ('C', 'E'), ('B', 'C')]
    print("Kruskal's tests passed!")




if __name__ == "__main__":
    simple_tree, complete_graph, disconnected_graph, varying_weights_graph, sparse_graph, cyclic_graph = createTestingKruskalsTrees()
    kruskalsChecker()