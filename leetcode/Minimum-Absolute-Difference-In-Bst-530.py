# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minv = [math.inf]
        prev = [None]

        def dfs(root):
            if not root:
                return

            dfs(root.left)

            if prev[0] is not None:
                minv[0] = min(minv[0], root.val-prev[0])

            prev[0] = root.val

            dfs(root.right)

        dfs(root)
        return minv[0]

# TC : O(n)
# SC : O(n)

# Suggested: Depth-First Search/Binary Search Tree
# Key Idea: Leveraging in-order traversal of a BST to visit nodes in sorted order for minimum difference calculation.
