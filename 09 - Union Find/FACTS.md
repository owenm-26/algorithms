# Algorithm Facts
Two different functions, one is `union()` the other is `find()`. We need to determine whether 2 nodes are in the same group with `find()` and we need to combine groups using `union()`. We will use this later in Kruskal's.

A node is the root of its group if it is the parent of itself.

## Time Complexity
O(logn) - Moving up the tree will typically cut the number of nodes in half each time 

## Space Complexity
O(n) - parent array has length n

<img src="https://i.ytimg.com/vi/ayW5B2W9hfo/maxresdefault.jpg" alt="union find"/>