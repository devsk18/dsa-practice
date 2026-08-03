# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        def preOrder(node):
            if not node:
                return
            
            res.append(node.val)
            preOrder(node.left)
            preOrder(node.right)

        preOrder(root)
        return res

# TC : O(n)
# SC : O(n)

# Suggested: Recursion/Tree
# Key Idea: Recursive depth-first traversal of a binary tree in root-left-right order.
# Consider: Since the follow-up asks for an iterative approach, how would you simulate the call stack using an explicit stack?
