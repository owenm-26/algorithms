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

    def stringifyResult(result):
        return {
        "dist": {repr(k): v for k, v in result["dist"].items()},
        "parents": {repr(k): repr(v) for k, v in result['parents'].items()}
    }

    expected_order = {'dist': {'Node 1': 0, 'Node 3': 1, 'Node 2': 1, 'Node 5': 2, 'Node 4': 2, 'Node 7': 2, 'Node 6': 2}, 'parents': {'Node 1': '[]', 'Node 3': '[Node 1]', 'Node 2': '[Node 1]', 'Node 5': '[Node 2]', 'Node 4': '[Node 2]', 'Node 7': '[Node 3]', 'Node 6': '[Node 3]'}}
    expected_backwards = {'dist': {'Node 9': 0, 'Node 7': 1, 'Node 8': 1, 'Node 5': 2, 'Node 6': 2, 'Node 3': 2, 'Node 4': 2}, 'parents': {'Node 9': '[]', 'Node 7': '[Node 9]', 'Node 8': '[Node 9]', 'Node 5': '[Node 8]', 'Node 6': '[Node 8]', 'Node 3': '[Node 7]', 'Node 4': '[Node 7]'}}
    expected_random = {'dist': {'Node 5': 0, 'Node 3': 1, 'Node 6': 1, 'Node 1': 2, 'Node 4': 2, 'Node 9': 2, 'Node 2': 2}, 'parents': {'Node 5': '[]', 'Node 3': '[Node 5]', 'Node 6': '[Node 5]', 'Node 1': '[Node 6]', 'Node 4': '[Node 6]', 'Node 9': '[Node 3]', 'Node 2': '[Node 3]'}}
   
    if bfsResults:
        assert stringifyResult(bfsResults["backwards"]) == expected_backwards
        assert stringifyResult(bfsResults["random"]) == expected_random
        assert stringifyResult(bfsResults["order"]) == expected_order
        return "BFS Tests Passed!"
    if dfsResults:
        assert stringifyResult(dfsResults["backwards"]) == expected_backwards
        assert stringifyResult(dfsResults["random"]) == expected_random
        assert stringifyResult(dfsResults["order"]) == expected_order
        return "DFS Tests Passed!"
    
def createTestingWeightedTrees():
    binary = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'D': 1, 'E': 3},
    'C': {'A': 5, 'F': 2},
    'D': {'B': 1},
    'E': {'B': 3},
    'F': {'C': 2}
}
    unbalanced = {
    'A': {'B': 4, 'C': 3},
    'B': {'A': 4, 'D': 2},
    'C': {'A': 3, 'E': 6},
    'D': {'B': 2, 'F': 1},
    'E': {'C': 6, 'G': 4},
    'F': {'D': 1},
    'G': {'E': 4}
}

    varyingWeights = {
    'A': {'B': 10, 'C': 1},
    'B': {'A': 10, 'D': 5, 'E': 1},
    'C': {'A': 1, 'F': 7, 'G': 3},
    'D': {'B': 5},
    'E': {'B': 1},
    'F': {'C': 7},
    'G': {'C': 3, 'H': 12},
    'H': {'G': 12}
}
    
    return binary, unbalanced, varyingWeights

def createTestingKruskalsTrees():
    simple_tree = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2},
    'C': {'A': 4},
    'D': {'B': 2}
}
    complete_graph = {
    'A': {'B': 1, 'C': 5, 'D': 4},
    'B': {'A': 1, 'C': 2, 'D': 3},
    'C': {'A': 5, 'B': 2, 'D': 1},
    'D': {'A': 4, 'B': 3, 'C': 1}
}

    disconnected_graph = {
    'A': {'B': 1},
    'B': {'A': 1, 'C': 2},
    'C': {'B': 2},
    'D': {'E': 3},
    'E': {'D': 3}
}
    varying_weights_graph = {
    'A': {'B': 3, 'C': 10, 'D': 4},
    'B': {'A': 3, 'D': 8, 'E': 5},
    'C': {'A': 10, 'F': 6},
    'D': {'A': 4, 'B': 8, 'F': 2},
    'E': {'B': 5, 'F': 9},
    'F': {'C': 6, 'D': 2, 'E': 9}
}
    
    sparse_graph = {
    'A': {'B': 2},
    'B': {'A': 2, 'C': 3},
    'C': {'B': 3},
    'D': {'E': 1},
    'E': {'D': 1}
}
    cyclic_graph = {
    'A': {'B': 1, 'C': 5},
    'B': {'A': 1, 'C': 4, 'D': 2},
    'C': {'A': 5, 'B': 4, 'E': 3},
    'D': {'B': 2, 'E': 6},
    'E': {'C': 3, 'D': 6}
}




    return simple_tree, complete_graph, disconnected_graph, varying_weights_graph, sparse_graph, cyclic_graph



if __name__ == "__main__":
    root = createTree([3,4,5,6,7,8,9,1])

    # print_tree(root)
