# Last updated: 1/2/2026, 12:18:50 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Base cases: empty list or single element or no rotation needed
        if head is None or head.next is None or k == 0:
            return head
        
        # Step 1: Compute the length of the list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Step 2: Normalize k (handle case where k >= length)
        k = k % length
        if k == 0:
            return head  # No rotation needed after adjustment

        # Step 3: Use two-pointer technique to find the new head
        slow = head
        fast = head
        
        # Move fast pointer k steps ahead
        for _ in range(k):
            fast = fast.next

        # Move both slow and fast until fast reaches the last node
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # Now, slow is at the node just before the new head
        new_head = slow.next
        slow.next = None      # Break the list
        fast.next = head      # Connect the end to the original head
        
        return new_head
