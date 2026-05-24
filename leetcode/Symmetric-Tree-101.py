# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isSame(root1, root2):
            if not root1 and not root2:
                return True
            
            if not root1 or not root2:
                return False
                
            if root1.val != root2.val:
                return False
            
            return isSame(root1.left, root2.right) and isSame(root2.left, root1.right)
        
        return isSame(root.left, root.right)
        
# TC : O(N)
# SC : O(h)

# Suggested: Recursion/Breadth-First Search/Binary Tree
# Key Idea: Checking binary tree symmetry by recursively comparing mirrored left and right subtrees.

