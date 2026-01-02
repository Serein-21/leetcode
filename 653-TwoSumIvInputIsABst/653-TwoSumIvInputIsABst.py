# Last updated: 1/2/2026, 12:17:53 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        # Convert BST to a doubly linked list (DLL) using in-order traversal
        def dll(root):
            if not root:
                return None, None
            
            lh, lt = dll(root.left)  # Recursively process the left subtree
            rh, rt = dll(root.right)  # Recursively process the right subtree

            # Connect the current node in DLL format
            if lh:
                l = lh
                lt.right = root  # Connect the rightmost node of the left subtree to root
                root.left = lt   # Connect the left of root to the left subtree's tail
            else:
                l = root

            if rh:
                r = rt
                root.right = rh  # Connect the right subtree to root
                rh.left = root   # Connect the left of the right subtree to root
            else:
                r = root

            return l, r  # Return the leftmost and rightmost nodes of the DLL
        
        # Get the leftmost and rightmost nodes of the DLL
        l, r = dll(root)

        # Use two-pointer technique to find if two numbers sum to k
        while l.val != r.val:
            total = l.val + r.val
            if total == k:
                return True  # We found two nodes with sum equal to k
            elif total < k:
                l = l.right  # Move the left pointer to the next node in the DLL
            else:
                r = r.left   # Move the right pointer to the previous node in the DLL
        
        return False  # No pair found with sum equal to k

            
        