# this was mostly chatgpt'd so I can work faster
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __repr__(self) -> str:
        return f"Node {self.value}"

    def __str__(self) -> str:
        return f"Node {self.value}"

def print_tree(root):
    def get_depth(node):
        if node is None:
            return 0
        return 1 + max(get_depth(node.left), get_depth(node.right))
    
    def fill_tree(root, tree, level=0, pos=0, max_level=0):
        if root is None:
            return
        width = 2 ** (max_level - level - 1)
        tree[level][pos * width] = '[' + str(root.value) + ']'
        if root.left:
            fill_tree(root.left, tree, level + 1, 2 * pos, max_level)
        if root.right:
            fill_tree(root.right, tree, level + 1, 2 * pos + 1, max_level)
    
    depth = get_depth(root)
    width = 2 ** depth - 1
    tree = [[' ' for _ in range(width)] for _ in range(depth)]
    fill_tree(root, tree, 0, 0, depth)
    
    for level in tree:
        print(''.join(level).center(width * 4 - 1))

def createTree(vals):
    root = TreeNode(vals[0])
    root.left = TreeNode(vals[1])
    root.right = TreeNode(vals[2])
    root.left.left = TreeNode(vals[3])
    root.left.right = TreeNode(vals[4])
    root.right.left = TreeNode(vals[5])
    root.right.right = TreeNode(vals[6])
    return root

def createTestingTrees():
    order = createTree([1,2,3,4,5,6,7])
    backwards = createTree([9,8,7,6,5,4,3,2,1])
    random = createTree([5,6,3,4,1,2,9,8,4])
    return [order, backwards, random]

# handles all testing for BFS and DFS
def testTraversal(bfsResults, dfsResults):

    expected_order = {'dist': {'Node 2': 1, 'Node 3': 1, 'Node 4': 2, 'Node 5': 2, 'Node 6': 2, 'Node 7': 2}, 'parents': {'Node 2': 'Node 1', 'Node 3': 'Node 1', 'Node 4': 'Node 2', 'Node 5': 'Node 2', 'Node 6': 'Node 3', 'Node 7': 'Node 3'}}
    expected_backwards = {'dist': {'Node 8': 1, 'Node 7': 1, 'Node 6': 2, 'Node 5': 2, 'Node 4': 2, 'Node 3': 2}, 'parents': {'Node 8': 'Node 9', 'Node 7': 'Node 9', 'Node 6': 'Node 8', 'Node 5': 'Node 8', 'Node 4': 'Node 7', 'Node 3': 'Node 7'}}
    expected_random = {'dist': {'Node 6': 1, 'Node 3': 1, 'Node 4': 2, 'Node 1': 2, 'Node 2': 2, 'Node 9': 2}, 'parents': {'Node 6': 'Node 5', 'Node 3': 'Node 5', 'Node 4': 'Node 6', 'Node 1': 'Node 6', 'Node 2': 'Node 3', 'Node 9': 'Node 3'}}
   
    if bfsResults:
        assert bfsResults["backwards"] == expected_backwards
        assert bfsResults["random"] == expected_random
        assert bfsResults["order"] == expected_order
        return "BFS Tests Passed!"
    if dfsResults:
        assert dfsResults["backwards"] == expected_backwards
        assert dfsResults["random"] == expected_random
        assert dfsResults["order"] == expected_order
        return "DFS Tests Passed!"

   



if __name__ == "__main__":
    root = createTree([3,4,5,6,7,8,9,1])

    print_tree(root)
