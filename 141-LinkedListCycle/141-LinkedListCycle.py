# Last updated: 1/2/2026, 12:18:41 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Create a set to store memory addresses of visited nodes
        visited_nodes = set()
        
        # Initialize the pointer to the head of the list
        pointer = head

        # Traverse the linked list
        while pointer:
            # Check if the current node has been visited before (cycle detected)
            if id(pointer) in visited_nodes:
                return True  # Cycle detected
            
            # Otherwise, add the current node's memory address to the set
            visited_nodes.add(id(pointer))
            
            # Move to the next node
            pointer = pointer.next
        
        # If the loop exits, no cycle is detected
        return False
