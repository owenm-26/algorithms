import sys
import os

# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

dfs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../06 -  DFS'))
sys.path.append(dfs_dir)

from dfs import iterativeDfs

from treeHelpers import createTestingTrees, print_tree, TreeNode

def topologicalSort(tree: TreeNode):
    result = iterativeDfs(tree)
    parents = result['parents']
    dist = result['dist']
    zeroIn = []
    ordering = []

    print(parents)
    for node in dist:
        print(len(parents[node]))
        if len(parents[node]) == 0:
            zeroIn.append(node)
    print(zeroIn)

    while len(zeroIn) > 0:
        next = zeroIn.pop()
        ordering.append(next)
        if next.left:
            parents[next.left].remove(next)
            if len(parents[next.left]) == 0:
                zeroIn.append(next.left)
        if next.right:
            parents[next.right].remove(next)
            if len(parents[next.right]) == 0:
                zeroIn.append(next.right)

    if len(ordering) < len(dist):
        return "No topological ordering possible"
    else:
        return ordering



def topologicalSortChecker():
    print(topologicalSort(order))

if __name__  == "__main__":
    order, backwards, random = createTestingTrees()
    topologicalSortChecker()