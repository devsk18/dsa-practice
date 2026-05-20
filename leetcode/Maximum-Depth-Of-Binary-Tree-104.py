 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        count_l = 0
        count_r = 0

        count_l += 1 + self.maxDepth(root.left)
        count_r += 1 + self.maxDepth(root.right)
        
        return max(count_l, count_r)

# TC : O(N)
# SC : O(H) - height of the btree

# Suggested: Recursion/Binary Tree/Depth-First Search
# Key Idea: Calculating maximum depth using recursive depth-first search to traverse left and right subtrees.
