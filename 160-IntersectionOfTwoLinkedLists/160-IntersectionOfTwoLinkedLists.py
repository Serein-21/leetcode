# Last updated: 1/2/2026, 12:18:37 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Initialize a set to store memory addresses of nodes in list A
        visited_nodes = set()
        
        # Traverse list A and add each node's memory address (id) to the set
        p = headA
        while p:
            visited_nodes.add(id(p))  # Store the id of each node in the set
            p = p.next
        
        # Traverse list B and check if any node's id is in the set
        q = headB
        while q:
            if id(q) in visited_nodes:  # Check if the current node of B is in the set
                return q  # Return the intersecting node
            q = q.next
        
        # If no intersection is found, return None
        return None
