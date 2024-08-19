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
    parents[root] = []
    visited = set()

    while stack:
        node = stack.pop()
        if node is not None:
            if node in visited:
                continue
            visited.add(node)
            if node.right:
                if node.right not in parents:
                    parents[node.right] = []
                parents[node.right].append(node)
                if node.right not in dist:
                    dist[node.right] = dist[node] + 1
                
                stack.append(node.right)
            if node.left:
                if node.left not in parents:
                    parents[node.left] = []
                parents[node.left].append(node)
                if node.left not in dist:
                    dist[node.left] = dist[node] + 1
                
                stack.append(node.left)
    
    # Convert node objects to their string representation for the return dictionary
    return{
        "dist": dist,
        "parents": parents
    }

def dfsChecker():
    order, backwards, random = createTestingTrees()
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
    
    dfsChecker()