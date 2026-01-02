# Last updated: 1/2/2026, 12:18:33 PM
from collections import deque
from typing import Optional, List

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def LevelOrderTraversal(root):
            if not root:
                return []

            smalllist, biglist = [], []
            q = deque([root, None])  # Start with the root node and a marker for the level

            while q:
                n = q.popleft()  # Use popleft for a cleaner level traversal

                if n:
                    smalllist.append(n.val)  # Append current node value
                    if n.left:
                        q.append(n.left)  # Add left child to the queue
                    if n.right:
                        q.append(n.right)  # Add right child to the queue
                else:
                    if smalllist:  # Check if smalllist is not empty
                        biglist.append(smalllist[-1])  # Add the last element of smalllist to biglist

                    if q:  # If there are more nodes to process
                        q.append(None)  # Add a marker for the next level

                    # Reset smalllist for the next level

            return biglist 

        return LevelOrderTraversal(root)
