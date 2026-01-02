# Last updated: 1/2/2026, 12:18:39 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
         result = []  # Use a proper variable name, not `list`
        
         def f(node):
            if node:  # If the current node exists
                f(node.left)  # Traverse the left subtree
                  # Append the current node's value
                f(node.right) 
                result.append(node.val) # Traverse the right subtree

         f(root)  # Start the traversal from the root
         return result  # Return the list of nodes in in-order


        