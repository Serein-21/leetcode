# Last updated: 1/2/2026, 12:18:27 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Inner function to recursively invert the tree
        def invert(root):
            if root:
                # Recursively invert the left and right subtrees
                invert(root.left)
                invert(root.right)

                # Swap the left and right children of the current node
                root.left, root.right = root.right, root.left
            
            return root

        # Call the inner function to invert the tree starting from the root
        return invert(root)
