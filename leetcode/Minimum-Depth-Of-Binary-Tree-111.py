# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        res = [math.inf]
        def minD(node, depth):
            if not node:
                return
            
            depth += 1
            if not node.left and not node.right:
                res[0] = min(res[0], depth)
                return

            minD(node.left, depth)
            minD(node.right, depth)

        minD(root, 0)
        return res[0] if res[0] != math.inf else 0

# TC : O(n)
# SC : O(n)

# Current: Depth-First Search/Recursion
# Suggested: Breadth-First Search/Depth-First Search
# Key Idea: Find the shortest path from root to any leaf node in a binary tree.
# Consider: Could BFS potentially find the answer faster than DFS in some scenarios?
