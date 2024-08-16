import sys
import os

# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from treeHelpers import createTestingTrees, TreeNode, print_tree, testTraversal

# for simply traversing
def recursiveDfs(root: TreeNode):
    if root is not None:
        recursiveDfs(root.left)
        print(root)
        recursiveDfs(root.right)

# in order dfs
def iterativeDfs(root: TreeNode):
    parents = {}
    dist = {}
    stack = [root]
    dist[root] = 0
    parents[root] = None

    while stack:
        node = stack.pop()
        if node is not None:
            if node.right:
                parents[node.right] = node
                dist[node.right] = dist[node] + 1
                stack.append(node.right)
            if node.left:
                parents[node.left] = node
                dist[node.left] = dist[node] + 1
                stack.append(node.left)
    
    # Convert node objects to their string representation for the return dictionary
    return {
        "dist": {repr(k): v for k, v in dist.items()},
        "parents": {repr(k): repr(v) for k, v in parents.items()}
    }

def dfsChecker():
    dfsOrder = iterativeDfs(order)
    dfsRandom = iterativeDfs(random)
    dfsBackwards = iterativeDfs(backwards)
    dfsResult = {"order": dfsOrder, "random": dfsRandom, "backwards": dfsBackwards}
    print(testTraversal(bfsResults=None, dfsResults=dfsResult))

    # print(print_tree(order))
    # print(iterativeDfs(order))
    # print(print_tree(backwards))
    # print(iterativeDfs(backwards))
    # print(print_tree(random))
    # print(iterativeDfs(random))

if __name__ == "__main__":
    trees = createTestingTrees()
    order = trees[0]
    backwards = trees[1]
    random = trees[2]
    dfsChecker()