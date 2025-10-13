from graphHelpers import createKByKGraph, GraphNode
from typing import List
from heapq import heappop, heappush
import math
import collections
import matplotlib.pyplot as plt
import numpy as np

def straightLineApproximation(source: List):
    assert source and len(source) == 2

    sum_of_squares = source[0]**2 + source[1]**2
    return math.sqrt(sum_of_squares)

def absoluteDistanceApproximation(source:List):
    assert source and len(source) == 2

    absolute_dist = source[0] + source[1]
    return absolute_dist

def modifiedDijkstras(graph: List[List[GraphNode]], startCoordinates: List):
    assert graph and len(startCoordinates) == 2 and startCoordinates[0] >= 0 and startCoordinates[1] >= 0
    s: GraphNode = graph[startCoordinates[0]][startCoordinates[1]]

    dist = {node: float('inf') for row in graph for node in row}
    dist[s] = 0
    explored = set()
    PQ = []
    heappush(PQ, (0, s))

    h = collections.defaultdict(int) 
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            h[graph[i][j]] = 0

    while PQ:
        du, u = heappop(PQ)
        if du > dist[u]:
            continue  # Skip outdated entry
        
        explored.add(u)
        # check if this is the node to escape for (0,0)
        if u == graph[0][0]:
            return explored

        for v in [u.up, u.down, u.left, u.right]:
            cost = 1 + h[v] - h[u]
            if v and dist[v] > du + cost:
                dist[v] = du + cost
                heappush(PQ, (dist[v], v))
    print("didn't find T?")
    return None

def plot_explored_nodes(explored_values, k=100):
    """
    explored_values: set or list of GraphNode.value (ints)
    k: grid size (k x k)
    """
    grid = np.zeros((k, k))

    for val in explored_values:
        i, j = divmod(val.value, k)
        grid[i, j] = 1  # mark explored

    plt.figure(figsize=(8, 8))
    plt.imshow(grid, cmap='Blues', origin='upper')
    plt.title(f"Explored Nodes in {k}x{k} Grid ({len(explored_values)} explored)")
    plt.xlabel("Column index (x)")
    plt.ylabel("Row index (y)")
    plt.grid(False)
    plt.show()
    plt.savefig()

if __name__ == "__main__":
    k = 100
    graph = createKByKGraph(k=k)
    coordinates = (k//2, k//3)
    res = modifiedDijkstras(graph=graph, startCoordinates=coordinates)

    print(len(res))
    plot_explored_nodes(explored_values=res)