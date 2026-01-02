# Last updated: 1/2/2026, 12:18:23 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def f(root, p, q):
            if root:
                # Check if root is the lowest common ancestor
                if p.val <= root.val <= q.val:
                    return root

                # If both p and q are smaller than root, LCA must be in the left subtree
                if q.val < root.val:
                    return f(root.left, p, q)

                # Otherwise, LCA must be in the right subtree
                return f(root.right, p, q)

        # Ensure that p is always the smaller and q is the larger node
        if p.val > q.val:
            p, q = q, p

        return f(root, p, q)
