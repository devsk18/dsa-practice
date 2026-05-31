# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = [root]
        def search(node):
            if node is None:
                return
            
            lca[0] = node

            if node is p or node is q:
                return
            elif node.val < p.val and node.val < q.val:
                search(node.right)
            elif node.val > p.val and node.val > q.val:
                search(node.left)
            else:
                return
        
        search(root)
        return lca[0]

# TC : O(h) height of the tree
# SC : O(h)

# Suggested: Binary Search Tree/Two Pointers
# Key Idea: Utilize BST property where LCA is the split point between two node values.

