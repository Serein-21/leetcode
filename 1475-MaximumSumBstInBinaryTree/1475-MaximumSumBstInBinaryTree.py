# Last updated: 1/2/2026, 12:17:38 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        global msum
        msum = 0  # To keep track of the maximum sum of any valid BST subtree
        
        def f(root):
            # Base case: If the node is None, return a large boundary to avoid false comparisons
            if not root:
                return (10**5, -10**5, 0)  # (min_val, max_val, sum) for an empty subtree
            
            # Recursively check the left and right subtrees
            lmin, lmax, lsum = f(root.left)
            rmin, rmax, rsum = f(root.right)
            
            # Check if the current subtree rooted at 'root' is a valid BST
            if lmax < root.val < rmin:
                # If valid, calculate the sum of the current subtree
                current_sum = lsum + rsum + root.val
                global msum
                msum = max(msum, current_sum)  # Update the maximum sum if the current one is larger
                
                # Return the updated min, max, and sum for the current subtree
                return (min(lmin, root.val), max(rmax, root.val), current_sum)
            
            # If not a valid BST, return invalid values (large min, small max) to break the BST condition
            return (-10**5, 10**5, 0)
        
        # Call the recursive function
        f(root)
        
        # Return the maximum sum found
        return msum
