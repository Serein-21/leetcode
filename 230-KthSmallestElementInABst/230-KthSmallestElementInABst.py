# Last updated: 1/2/2026, 12:18:26 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.i = 0  # Initialize the counter as a class instance attribute
        self.n = None  # Initialize the result as a class instance attribute
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def solve(root, k):
            if root:
                # Traverse the left subtree first (in-order traversal)
                solve(root.left, k)
                
                # Increment the counter when visiting a node
                self.i += 1
                
                # If the counter reaches 'k', store the value of the node
                if self.i == k:
                    self.n = root.val
                    return
                
                # Traverse the right subtree
                solve(root.right, k)

        solve(root, k)
        return self.n
