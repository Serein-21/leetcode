# Last updated: 1/2/2026, 12:17:44 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        # Helper function to recursively calculate the sum
        def solve(root, curr_sum):
            if root:
                # Update the current sum by shifting left and adding the node's value
                curr_sum = 2 * curr_sum + root.val

                # If it's a leaf node, return the current sum
                if not root.left and not root.right:
                    return curr_sum

                # Otherwise, return the sum of the left and right subtrees
                return (solve(root.left, curr_sum) + solve(root.right, curr_sum))
            
            # If the node is None, return 0 (this handles the case for empty child nodes)
            return 0

        # Call the helper function starting with root and 0 as the initial sum
        return solve(root, 0)
