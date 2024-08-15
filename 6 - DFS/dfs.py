import sys
import os

# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from treeHelpers import createTestingTrees, TreeNode, print_tree, testTraversal

def recursiveDfs(root: TreeNode):
    if root is not None:
        recursiveDfs(root.left)
        print(root)
        recursiveDfs(root.right)

# in order dfs
def iterativeDfs(root: TreeNode):
    parents = {}
    dist = {}
    parents[root] = None
    dist[root] = 0
    stack = []
    stack.append(root)

    while len(stack) > 0:
        node = stack.pop()
        if node!= root:
            dist[node] = dist[parents[node]]+1
        if node is not None:
            # do right first so that left is on top of stack
            if node.right:
                parents[node.right] = node
                stack.append(node.right)
            if node.left:
                parents[node.left] = node
                stack.append(node.left)
    
    return {"dist": dist, "parents": parents}
        
        



def dfsChecker():
    # print(print_tree(order))
    # print(iterativeDfs(order))
    # print(print_tree(backwards))
    # print(iterativeDfs(backwards))
    # print(print_tree(random))
    # print(iterativeDfs(random))
    dfsOrder = iterativeDfs(order)
    dfsRandom = iterativeDfs(random)
    dfsBackwards = iterativeDfs(backwards)
    bfsResults = {"order": dfsOrder, "random": dfsRandom, "backwards": dfsBackwards}
    print(testTraversal(bfsResults=bfsResults, dfsResults=None))

if __name__ == "__main__":
    trees = createTestingTrees()
    order = trees[0]
    backwards = trees[1]
    random = trees[2]
    dfsChecker()