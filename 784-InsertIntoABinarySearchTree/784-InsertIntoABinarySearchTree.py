# Last updated: 1/2/2026, 12:17:51 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def traverse(node, val):
            # Traverse the tree and insert without returning anything
            if val < node.val:
                # If the left child is None, we insert the value here
                if node.left is None:
                    node.left = TreeNode(val)
                else:
                    # Otherwise, continue traversing the left subtree
                    traverse(node.left, val)
            elif val > node.val:
                # If the right child is None, we insert the value here
                if node.right is None:
                    node.right = TreeNode(val)
                else:
                    # Otherwise, continue traversing the right subtree
                    traverse(node.right, val)
        
        # If the tree is empty, we create the root node with the given value
        if root is None:
            return TreeNode(val)
        
        # Traverse and insert the value into the correct position
        traverse(root, val)
        
        # Return the original root (not modified or reassigned, but updated)
        return root
