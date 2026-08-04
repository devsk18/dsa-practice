# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def postOrder(node):
            if not node:
                return
            
            postOrder(node.left)
            postOrder(node.right)

            res.append(node.val)
        
        postOrder(root)
        return res

# TC : O(n)
# SC : O(n)

# Suggested: Tree/Stack/Depth-First Search
# Key Idea: Postorder traversal visits left subtree, right subtree, then root node.
# Consider: Can you implement this iteratively using a stack to avoid recursion overhead?
