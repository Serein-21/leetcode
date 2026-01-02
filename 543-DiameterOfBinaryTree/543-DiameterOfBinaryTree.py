# Last updated: 1/2/2026, 12:18:01 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def f(root):
            if not root:
                return 0, 0  # Return height 0 and diameter 0 for an empty subtree
            
            # Recursively compute the left and right subtree heights and diameters
            lh, ld = f(root.left)
            rh, rd = f(root.right)
            
            # Current height is 1 + max of left and right subtree heights
            height = 1 + max(lh, rh)
            
            # The diameter at this node is the maximum of:
            # 1. The current diameter passing through the node (lh + rh)
            # 2. The best diameter in the left subtree (ld)
            # 3. The best diameter in the right subtree (rd)
            diameter = max(ld, rd, lh + rh)
            
            return height, diameter
        
        return f(root)[1]  # Return only the diameter part of the result
