import sys
import os
from heapq import heappop, heappush

# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from treeHelpers import createTestingWeightedTrees

# graph is an adjacency list to represented the weighted edges
def dijkstra(graph, source):

    if source not in graph:
        return 'Invalid Input. Source not in graph'
    
    pi = {} # hash table current best from s to v
    parents = {} # hash table, parents in shortest path

    PQ = []
    heappush(PQ, (0,source))

    dist = {} # hash table, final distance to v 

    # assign infinity to all nodes initial distances and add to heap
    for node in graph:
        if node is not source:
            pi[node] = float('inf')
            heappush(PQ, (pi[node], node))
    
    # set vals for source
    pi[source] = 0
    dist[source] = 0
    parents[source] = None

    while PQ:
        best_dist, u = heappop(PQ)
        if best_dist > pi[u]:
            continue
        dist[u] = best_dist
        for v in graph[u]:
            newWeight = dist[u] + graph[u][v]
            if newWeight < pi[v]:
                pi[v] = newWeight
                heappush(PQ, (pi[v], v))
                parents[v] = u
    
    return dist, parents

def dijkstraChecker():
    assert dijkstra(binary, 'A') == ({'A': 0, 'B': 2, 'D': 3, 'C': 5, 'E': 5, 'F': 7}, {'A': None, 'B': 'A', 'C': 'A', 'D': 'B', 'E': 'B', 'F': 'C'})
    assert dijkstra(unbalanced, 'A') == ({'A': 0, 'C': 3, 'B': 4, 'D': 6, 'F': 7, 'E': 9, 'G': 13}, {'A': None, 'B': 'A', 'C': 'A', 'E': 'C', 'D': 'B', 'F': 'D', 'G': 'E'})
    assert dijkstra(varyingWeights, 'A') == ({'A': 0, 'C': 1, 'G': 4, 'F': 8, 'B': 10, 'E': 11, 'D': 15, 'H': 16}, {'A': None, 'B': 'A', 'C': 'A', 'F': 'C', 'G': 'C', 'H': 'G', 'D': 'B', 'E': 'B'})
    assert dijkstra(varyingWeights, 'Z') == 'Invalid Input. Source not in graph'
    print('Dijkstra tests passed!')

if __name__ == '__main__':
    binary, unbalanced, varyingWeights = createTestingWeightedTrees()
    dijkstraChecker()