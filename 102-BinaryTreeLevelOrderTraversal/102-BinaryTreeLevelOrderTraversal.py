# Last updated: 1/2/2026, 12:18:45 PM
from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []  # If the tree is empty, return an empty list.
        
        q = deque([root])  # Start with just the root in the queue.
        FinalList = []  # List to store the final level-order traversal
        
        while q:
            level_size = len(q)  # Track the number of nodes in the current level
            current_level = []  # List to store nodes of the current level
            
            for _ in range(level_size):  # Process all nodes in the current level
                node = q.popleft()  # Get the node from the front of the deque
                current_level.append(node.val)  # Add its value to the current level
                
                # Add the left and right children to the queue for the next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            FinalList.append(current_level)  # Add the current level to the final result
        
        return FinalList
