from helpers import createTree, print_tree
def bfs(root):
    dist = {}
    parents = {}
    layers = {}
    layers[0] = [root]

    i = 0
    while layers[i]:
        layers[i+1] = []
        for u in layers[i]:
            if u.left:
                parents[f'Node {u.left.value}'] = f"Node {u.value}"
                dist[f'Node {u.left.value}'] = i+1
                layers[i+1].append(u.left)
            if u.right:
                parents[f"Node {u.right.value}"] = f"Node {u.value}"
                dist[f"Node {u.right.value}"] = i+1
                layers[i+1].append(u.right)
        i += 1
    
    return {'dist': dist, 'parents': parents}

def bfsChecker():
    # print(print_tree(order))
    # print(bfs(order))
    # print(print_tree(backwards))
    # print(bfs(backwards))
    # print(print_tree(random))
    # print(bfs(random))
    assert bfs(order) == {'dist': {'Node 2': 1, 'Node 3': 1, 'Node 4': 2, 'Node 5': 2, 'Node 6': 2, 'Node 7': 2}, 'parents': {'Node 2': 'Node 1', 'Node 3': 'Node 1', 'Node 4': 'Node 2', 'Node 5': 'Node 2', 'Node 6': 'Node 3', 'Node 7': 'Node 3'}}
    assert bfs(backwards) == {'dist': {'Node 8': 1, 'Node 7': 1, 'Node 6': 2, 'Node 5': 2, 'Node 4': 2, 'Node 3': 2}, 'parents': {'Node 8': 'Node 9', 'Node 7': 'Node 9', 'Node 6': 'Node 8', 'Node 5': 'Node 8', 'Node 4': 'Node 7', 'Node 3': 'Node 7'}}
    assert bfs(random) == {'dist': {'Node 6': 1, 'Node 3': 1, 'Node 4': 2, 'Node 1': 2, 'Node 2': 2, 'Node 9': 2}, 'parents': {'Node 6': 'Node 5', 'Node 3': 'Node 5', 'Node 4': 'Node 6', 'Node 1': 'Node 6', 'Node 2': 'Node 3', 'Node 9': 'Node 3'}}
    print('BFS Tests Passed!')


if __name__ == '__main__':
    order = createTree([1,2,3,4,5,6,7])
    backwards = createTree([9,8,7,6,5,4,3,2,1])
    random = createTree([5,6,3,4,1,2,9,8,4])
    bfsChecker()