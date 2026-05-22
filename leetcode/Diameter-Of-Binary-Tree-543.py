# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest_diameter = [0]
 
        def height(root):
            if root is None:
                return 0
 
            left_height = height(root.left)
            right_height = height(root.right)
            diameter = left_height + right_height
 
            largest_diameter[0] = max(largest_diameter[0], diameter)
            
            return 1 + max(left_height, right_height)
 
        height(root)
        return largest_diameter[0]

# TC : O(N)
# SC : O(h)

# Suggested: Depth-First Search/Recursion
# Key Idea: Calculating tree diameter by tracking max path sum during recursive height computation.
