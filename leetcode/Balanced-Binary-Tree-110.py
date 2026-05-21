# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]
        
        def depth(root):
            if not root:
                return 0
        
            count_l = depth(root.left)
            if not balanced[0]:
                return 0

            count_r = depth(root.right)
            if abs(count_l-count_r) > 1:
                balanced[0] = False
                return 0

            return 1 + max(count_l, count_r)
        depth(root)
        return balanced[0]

# TC : O(N)
# SC : O(h)


# Suggested: Depth-First Search/Recursion
# Key Idea: Determining tree balance by computing heights bottom-up while pruning early upon detecting imbalance.
# Consider: Can you refactor this to return a special integer instead of using a list flag for even cleaner logic?
