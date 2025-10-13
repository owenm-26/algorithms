import typing
class GraphNode:
    def __init__(self, value=0):
        self.value = value
        self.up = None
        self.down = None
        self.left = None
        self.right = None

    def __repr__(self):
        return f"GraphNode({self.value})"
    def __lt__(self, other):
        return self.value < other.value


def createKByKGraph(k: int) -> typing.List[typing.List[GraphNode]]:
    """
    Creates a k x k grid of GraphNodes.
    Each node is connected to its neighbors: up, down, left, and right.
    Returns the top-left node (0,0) as the entry point.
    """
    if k <= 0:
        return None

    # Step 1: Create a 2D list (matrix) of nodes
    grid = [[GraphNode(i * k + j) for j in range(k)] for i in range(k)]

    # Step 2: Connect the nodes
    for i in range(k):
        for j in range(k):
            node = grid[i][j]
            if i > 0:
                node.up = grid[i - 1][j]
            if i < k - 1:
                node.down = grid[i + 1][j]
            if j > 0:
                node.left = grid[i][j - 1]
            if j < k - 1:
                node.right = grid[i][j + 1]

    # Step 3: Return the top-left node
    return grid