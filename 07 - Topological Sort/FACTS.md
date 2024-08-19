# Algorithm Facts
In a directed acyclical graph, there is/are specific ordering(s) such that you can visit each node. This is because edges are one directional. Every DAG must have one of these. This means we can tests for cycles by running topological sort and seeing if the length of the list is the same length as the number of nodes in the original graph.

## Time Complexity
O(n+m) - we visit every node and every edge in the graph because as each node we decrease its indegree

## Space Complexity
O(n+m) - the input is a graph of n nodes and m edges 

<img src="https://assets.leetcode.com/users/images/63bd7ad6-403c-42f1-b8bb-2ea41e42af9a_1613794080.8115625.png" alt="topoloical sort"/>