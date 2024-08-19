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
    # map alpha to num
    nodes = list(graph.keys())
    node_to_index = {node: i for i, node in enumerate(nodes)}
    index_to_node = {i: node for node, i in node_to_index.items()}

    # sort edge weights in increasing order
    PQ = []
    for u in graph:
        u_index = node_to_index[u]
        for v in graph[u]:
            v_index = node_to_index[v]
            heappush(PQ, [graph[u][v],u_index,v_index])
    MST = []
    n = len(graph)
    djs = DisjointSet(n)

    while len(MST) != n-1 and PQ:
        weight, u, v = heappop(PQ)
        if djs.find(u) == djs.find(v):
            continue
        else:
            MST.append((index_to_node[u], index_to_node[v], weight))
            djs.union(u,v)
    
    return MST

def kruskalsChecker():
    simple_tree, complete_graph, disconnected_graph, varying_weights_graph, sparse_graph, cyclic_graph = createTestingKruskalsTrees()
    assert kruskals(simple_tree) == [('A', 'B', 1), ('B', 'D', 2), ('A', 'C', 4)]
    assert kruskals(complete_graph) == [('A', 'B', 1), ('C', 'D', 1), ('B', 'C', 2)]
    assert kruskals(disconnected_graph) == [('A', 'B', 1), ('B', 'C', 2), ('D', 'E', 3)]
    assert kruskals(varying_weights_graph) == [('D', 'F', 2), ('A', 'B', 3), ('A', 'D', 4), ('B', 'E', 5), ('C', 'F', 6)]
    assert kruskals(sparse_graph) == [('D', 'E', 1), ('A', 'B', 2), ('B', 'C', 3)]
    assert kruskals(cyclic_graph) == [('A', 'B', 1), ('B', 'D', 2), ('C', 'E', 3), ('B', 'C', 4)]
    print("Kruskal's tests passed!")




if __name__ == "__main__":
    kruskalsChecker()