# Last updated: 1/2/2026, 12:18:57 PM
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node before head to simplify edge cases (e.g., removing the first node)
        dummy = ListNode(0, head)
        
        # Two pointers - start both at dummy
        fast = slow = dummy

        # Move fast n+1 steps ahead so there's a gap of n nodes between fast and slow
        for _ in range(n + 1):
            fast = fast.next

        # Move both fast and slow until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Now, slow is just before the node to delete
        slow.next = slow.next.next

        # Return the head (which might have changed if first node was removed)
        return dummy.next
