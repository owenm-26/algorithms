# this was mostly chatgpt'd so I can work faster
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

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

if __name__ == "__main__":
    root = createTree([3,4,5,6,7,8,9,1])

    print_tree(root)
