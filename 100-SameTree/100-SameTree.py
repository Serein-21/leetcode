# Last updated: 1/2/2026, 12:18:44 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Define the recursive function to solve the problem
        def solve(p, q):
            # If one of the nodes is None and the other is not, trees are not the same
            if (p and not q) or (q and not p):
                return False
            
            # If both nodes are None, they are the same at this point
            if not p and not q:
                return True

            # Check if current nodes have the same value, and recursively check their left and right children
            if p.val == q.val and solve(p.left, q.left) and solve(p.right, q.right):
                return True
            else:
                return False

        # Call the recursive function
        return solve(p, q)
