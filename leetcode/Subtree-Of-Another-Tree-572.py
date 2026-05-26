# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(p, q):
            if not p and not q:
                return True
            
            if (not p and q) or (not q and p):
                return False
            
            if p.val != q.val:
                return False
            
            return is_same(p.left, q.left) and is_same(p.right, q.right)

        def has_subtree(root):
            if not root:
                return False

            if is_same(root, subRoot):
                return True
            
            return has_subtree(root.right) or has_subtree(root.left)
        
        return has_subtree(root)

# TC : O(M * N)
# SC : O(N)

# Depth-First Search/Recursion/String Matching
# Key Idea: Verify subtree existence by recursively comparing tree structures via depth-first traversal.
