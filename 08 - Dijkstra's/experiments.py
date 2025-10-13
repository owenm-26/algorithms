from graphHelpers import createKByKGraph, GraphNode
from typing import List
from heapq import heappop, heappush

def modifiedDijkstras(graph: List[List[GraphNode]], startCoordinates: List):
    assert graph and len(startCoordinates) == 2 and startCoordinates[0] >= 0 and startCoordinates[1] >= 0
    s: GraphNode = graph[startCoordinates[0]][startCoordinates[1]]

    dist = {node: float('inf') for row in graph for node in row}
    dist[s] = 0
    PQ = []
    heappush(PQ, (0, s))

    while PQ:
        du, u = heappop(PQ)
        if du > dist[u]:
            continue  # Skip outdated entry

        # check if this is the node to escape for (0,0)
        if u == graph[0][0]:
            return dist.keys()

        for v in [u.up, u.down, u.left, u.right]:
            if v and dist[v] > du + 1:
                dist[v] = du + 1
                heappush(PQ, (dist[v], v))
    print("didn't find T?")
    return None
    

if __name__ == "__main__":
    k = 100
    graph = createKByKGraph(k=k)
    coordinates = (k//2, k//3)
    res = modifiedDijkstras(graph=graph, startCoordinates=coordinates)

    print(len(res))