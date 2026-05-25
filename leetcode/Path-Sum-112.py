# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def t_sum(root, cur_sum):
            if not root:
                return False
            
            cur_sum += root.val

            if not root.left and not root.right:
                return cur_sum == targetSum

            return t_sum(root.left, cur_sum) or t_sum(root.right, cur_sum)
        
        return t_sum(root, 0)

# TC : O(N)
# SC : O(H)

# Suggested: Depth-First Search/Recursion
# Key Idea: Using Depth-First Search to traverse root-to-leaf paths while accumulating sums to match a target value.
