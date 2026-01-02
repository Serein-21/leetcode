# Last updated: 1/2/2026, 12:18:02 PM
from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        def LevelOrderTraversal(root):
            if not root:
                return 0  # Handle the case where the tree is empty

            smalllist, biglist = [], []  # Initialize lists to store values
            q = deque([root, None])  # Start with the root node and a marker for the level

            while q:
                n = q.popleft()  # Use popleft for a cleaner level traversal

                if n:
                    smalllist.append(n.val)  # Append current node value
                    # Add child nodes to the queue for the next level
                    if n.left:
                        q.append(n.left)  # Add left child to the queue
                    if n.right:
                        q.append(n.right)  # Add right child to the queue
                else:
                    if smalllist:  # Check if smalllist is not empty
                        biglist.append(smalllist[0])  # Add the first element of smalllist to biglist (leftmost)

                    if q:  # If there are more nodes to process
                        q.append(None)  # Add a marker for the next level

                    # Reset smalllist for the next level
                    smalllist.clear()

            return biglist[-1] if biglist else 0  # Return the last recorded leftmost value from biglist

        return LevelOrderTraversal(root)  # Call the traversal function

# Example usage
# Constructing a binary tree for testing
#         2
#       /   \
#      1     3
#     /
#    4

