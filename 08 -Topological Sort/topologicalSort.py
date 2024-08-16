import sys
import os

# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from dfs import iterativeDfs

from treeHelpers import createTestingTrees, print_tree, TreeNode

def topologicalSort(tree: TreeNode):
    parents, dist = iterativeDfs(tree)
    zeroIn = []
    ordering = []

    for node in dist:
        if parents[node] == None:
            zeroIn.append(node)
    
    while len(zeroIn) > 0:
        next = zeroIn.pop()
        if next.left:
            parents[next.left][next] = None
            if parents[next.left] == None:
                zeroIn.append(next.left)



def topologicalSortChecker():
    pass

if __name__  == "__main__":
    topologicalSortChecker()