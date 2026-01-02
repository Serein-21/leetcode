# Last updated: 1/2/2026, 12:17:26 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        if not root.left and not root.right:
            return bool(root.val)
        
        # Recursive case: Evaluate the left and right children
        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)
        
        # Apply the operation based on the value of the current node
        if root.val == 2:  # OR operation
            return left_val or right_val
        elif root.val == 3:  # AND operation
            return left_val and right_val


     

        



                    

                    






        