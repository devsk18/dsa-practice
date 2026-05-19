# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur = root

        if not cur:
            return

        cur.left, cur.right = cur.right, cur.left
        self.invertTree(cur.left)
        self.invertTree(cur.right)

        return root

# TC : O(N)
# SC : O(h) - height of the tree

# Suggested: Recursion/Binary Tree
# Key Idea: Inverting a binary tree by recursively swapping left and right children of every node.
