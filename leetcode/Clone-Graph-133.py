"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        start = node
        map = {}
        stk = [node]
        visited = set()
        visited.add(node)

        while stk:
            node = stk.pop()
            map[node] = Node(val=node.val)
            
            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stk.append(nei)
        
        for old_node, new_node in map.items():
            for nei in old_node.neighbors:
                node = map[nei]
                new_node.neighbors.append(node)
        
        return map[start]
        
# TC: O(V + E)
# SC: O(V)

# Suggested: Depth-First Search/Hash Table
# Key Idea: Graph cloning using DFS traversal and a hash map to track visited nodes and prevent cycles.
# Consider: Could you refactor this logic to use a single pass with recursion or a queue instead of two separate loops?
