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

    i = 0
    while layers[i]:
        layers[i+1] = []
        for u in layers[i]:
            if u.left:
                parents[repr(u.left)] = repr(u)
                dist[repr(u.left)] = i + 1
                layers[i+1].append(u.left)
            if u.right:
                parents[repr(u.right)] = repr(u)
                dist[repr(u.right)] = i + 1
                layers[i+1].append(u.right)
        i += 1
    
    return {'dist': dist, 'parents': parents}

def bfsChecker():
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
    trees = createTestingTrees()
    order = trees[0]
    backwards = trees[1]
    random = trees[2]
    bfsChecker()