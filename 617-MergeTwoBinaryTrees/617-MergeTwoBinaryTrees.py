# Last updated: 1/2/2026, 12:17:55 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Helper function to merge the trees recursively
        def solve(root1, root2):
            if not root1:
                return root2
            if not root2:
                return root1

            # Create a new TreeNode by summing the values of root1 and root2
            root = TreeNode(root1.val + root2.val)
            
            # Recursively merge the left and right subtrees
            root.left = solve(root1.left, root2.left)
            root.right = solve(root1.right, root2.right)
            
            return root

        # Call the solve function and return the merged tree
        return solve(root1, root2)
