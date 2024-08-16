import sys
import os

# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

dfs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../06 -  DFS'))
sys.path.append(dfs_dir)

from dfs import iterativeDfs

from treeHelpers import createTestingTrees, TreeNode, createTree

def topologicalSort(tree: TreeNode):
    result = iterativeDfs(tree)
    parents = result['parents']
    dist = result['dist']
    zeroIn = []
    ordering = []
    
    for node in dist:
        if len(parents[node]) == 0:
            zeroIn.append(node)
    
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
    def stringifyListItems(result):
        for i in range(len(result)):
            result[i] = str(result[i])
        return result
    
    assert topologicalSort(nonDAG) == 'No topological ordering possible'
    assert stringifyListItems(topologicalSort(order)) == ['Node 1', 'Node 3', 'Node 7', 'Node 6', 'Node 2', 'Node 5', 'Node 4']
    assert stringifyListItems(topologicalSort(backwards)) == ['Node 9', 'Node 7', 'Node 3', 'Node 4', 'Node 8', 'Node 5', 'Node 6']
    assert stringifyListItems(topologicalSort(random)) == ['Node 5', 'Node 3', 'Node 9', 'Node 2', 'Node 6', 'Node 1', 'Node 4']
    print('Topological Sort tests passed!')
if __name__  == "__main__":
    order, backwards, random = createTestingTrees()
    nonDAG = createTree([1,2,3,4,5,6,7,8])
    nonDAG.left.left = nonDAG
    topologicalSortChecker()