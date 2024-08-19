import sys
import os

# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from treeHelpers import createTestingTrees, print_tree, testTraversal
def bfs(root):
    dist = {}
    parents = {}
    layers = {}
    layers[0] = [root]
    parents[root] = []
    dist[root] = 0

    i = 0
    while layers[i]:
        layers[i+1] = []
        for u in layers[i]:
            if u.left:
                if u.left not in parents:
                    parents[u.left] = []
                parents[u.left].append(u)
                
                if u.left not in dist:
                    dist[u.left] = dist[u] + 1
                layers[i+1].append(u.left)
            if u.right:
                if u.right:
                    if u.right not in parents:
                        parents[u.right] = []
                    parents[u.right].append(u)
                    
                    if u.right not in dist:
                        dist[u.right] = dist[u] + 1
                    layers[i+1].append(u.right)
        i += 1
    
    return {
        "dist": dist,
        "parents": parents
    }

def bfsChecker():
    order, backwards, random = createTestingTrees()
    # print(print_tree(order))
    # print(bfs(order))
    # print(print_tree(backwards))
    # print(bfs(backwards))
    # print(print_tree(random))
    # print(bfs(random))
    
    bfsOrder = bfs(order)
    bfsRandom = bfs(random)
    bfsBackwards = bfs(backwards)
    bfsResults = {"order": bfsOrder, "random": bfsRandom, "backwards": bfsBackwards}
    print(testTraversal(bfsResults=bfsResults, dfsResults=None))


if __name__ == '__main__': 
    bfsChecker()